import os
import httpx
import gradio as gr
import pandas as pd
import sqlite3
import re
from typing import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

# 🔐 Load key from HF Space secrets (Settings → Secrets)
OPENROUTER_KEY = os.getenv("OPENAI_API_KEY")
if not OPENROUTER_KEY:
    raise ValueError("❌ OPENAI_API_KEY not found in environment.")

# 🔄 Global in-memory DB
conn = sqlite3.connect(":memory:", check_same_thread=False)
globals()["agent_conn"] = conn

# 📥 CSV Loader
def load_csv_to_sqlite(file):
    try:
        df = pd.read_csv(file.name)
        conn = sqlite3.connect(":memory:", check_same_thread=False)
        df.to_sql("data", conn, index=False, if_exists="replace")
        globals()["agent_conn"] = conn
        return f"✅ Loaded {len(df)} rows into SQLite."
    except Exception as e:
        return f"❌ Error loading CSV: {e}"

# 🤖 NL → SQL
def nl_to_sql_node(state):
    question = state["question"]
    conn = globals().get("agent_conn")
    if not conn:
        return {"sql": "", "question": question, "error": "No DB connection"}

    schema = pd.read_sql("SELECT sql FROM sqlite_master WHERE type='table'", conn)
    schema_str = "\n".join(schema["sql"])
    sample = pd.read_sql("SELECT * FROM data LIMIT 3", conn).to_markdown()

    prompt = f"""
You are a helpful SQL assistant.
Given the table schema and sample rows, write a SQL query that answers the user's question.
Schema:
{schema_str}
Sample Rows:
{sample}
User Question:
{question}
SQL:
"""

    response = httpx.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_KEY}"},
        json={
            "model": "mistralai/mistral-small-3.2-24b-instruct:free",
            "messages": [{"role": "user", "content": prompt}],
        },
    )

    full_response = response.json()["choices"][0]["message"]["content"]

    # 🔎 Extract SQL from ```sql ... ``` block
    matches = re.findall(r"```sql\s*(.*?)```", full_response, re.DOTALL | re.IGNORECASE)

    if matches:
        sql = matches[0].strip()
    else:
        lines = full_response.strip().splitlines()
        sql_lines = [line for line in lines if line.strip().lower().startswith(("select", "with"))]
        sql = "\n".join(sql_lines).strip()

    return {"sql": sql, "question": question}

# 🧪 SQL Execution
def execute_sql_node(state):
    conn = globals().get("agent_conn")
    if not conn:
        return {"answer": "❌ No database loaded yet."}
    try:
        df = pd.read_sql(state["sql"], conn)
        return {"answer": df.to_markdown()}
    except Exception as e:
        return {"answer": f"❌ SQL Error: {e}"}

# 🔁 LangGraph setup
class AgentState(TypedDict):
    question: str
    sql: str
    answer: str

workflow = StateGraph(AgentState)
workflow.add_node("generate_sql", nl_to_sql_node)
workflow.add_node("run_query", execute_sql_node)
workflow.set_entry_point("generate_sql")
workflow.add_edge("generate_sql", "run_query")
workflow.add_edge("run_query", END)
graph = workflow.compile()

# 🎛️ Gradio UI
def handle_question(question):
    state = {"question": question}
    result = graph.invoke(state)
    return result.get("sql", ""), result.get("answer", "⚠️ No answer returned.")

with gr.Blocks(title="AI SQL Agent") as demo:
    gr.Markdown(
        """
        ## 🔍 AI SQL Agent (Powered by LangGraph + Mistral)
        Upload a CSV and ask anything in natural language.  
        _May take a few seconds to generate and run the query._
        """
    )

    with gr.Row():
        file = gr.File(label="📁 Upload CSV", file_types=[".csv"])
        file_output = gr.Textbox(label="Load Status", interactive=False)

    with gr.Row():
        q = gr.Textbox(label="❓ Ask a Question", placeholder="e.g., Who is the campus mantri from BIT Patna?")
        sql_box = gr.Textbox(label="🧾 Generated SQL", lines=2, interactive=False)
        a = gr.Textbox(label="💬 Answer", lines=8, interactive=False)

    file.upload(load_csv_to_sqlite, inputs=file, outputs=file_output)
    q.submit(handle_question, inputs=q, outputs=[sql_box, a])

demo.launch()
