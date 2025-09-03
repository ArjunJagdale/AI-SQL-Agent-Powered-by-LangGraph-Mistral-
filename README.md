# 📊 AI CSV → SQL Agent

An interactive agent that lets you upload a CSV file, ask questions in plain English, and get **natural language answers** (instead of raw tables).

Behind the scenes, the agent:

* ✅ Converts questions → **SQL queries**
* ⚡ Executes SQL on your CSV (in-memory SQLite)
* 🗣️ Translates results into **concise answers**
* 🔗 Uses **LangGraph** to **structure multi-step reasoning** and make SQL generation + interpretation more reliable
* 🏗️ Follows the **MCP (Model–Controller–Processor)** architectural pattern for clean modularity

---
## Demo - 

Try it live on Hugging Face Spaces:  
[AI CSV Agent on Hugging Face Spaces](https://huggingface.co/spaces/ajnx014/Natural-Language-to-SQL-Agent)

---
### Video

https://github.com/user-attachments/assets/e575c257-e161-4425-9999-4a4114b67df0


---

## 🏗️ Architecture (MCP = Model–Controller–Processor)

⚠️ Note: here **MCP = Model–Controller–Processor**, not Anthropic’s *Model Context Protocol*.

* **Processor (`processor.py`)**

  * Loads CSVs, validates structure, cleans column names.
  * Stores data in an **in-memory SQLite database**.
  * Provides dataset info and HTML helpers (for tables, errors, cards).

* **Model (`model.py`) + LangGraph**

  * The **LLM brain** of the system.
  * **LangGraph** provides a *graph-based workflow engine* for orchestrating steps like:

    1. **Interpretation** – Parse the user’s natural language question into structured intent.
    2. **SQL Generation** – Ask the LLM to generate a valid SQLite query.
    3. **Validation** – Sanitize SQL (allow only `SELECT`, check schema, reject unsafe ops).
    4. **Execution** – Run the query against the SQLite database.
    5. **Summarization** – Convert raw query results into a **clear natural-language answer**.
  * LangGraph makes this robust by treating each step as a **node in a graph** → you can retry, branch, or recover gracefully when something fails.
  * Example: If SQL generation fails, LangGraph can automatically re-prompt the LLM with more schema details before moving forward.

* **Controller (`controller.py`)**

  * Orchestrates between Processor & Model.
  * Manages dataset stats, query history, and HTML formatting.
  * Adds guardrails for empty inputs or failed queries.

* **App (`app.py`)**

  * **Gradio UI** for uploads, queries, results, SQL preview, and history.
  * Includes helpful tips + example queries.

---

## 🚀 Why LangGraph?

LangGraph is key here because natural language → SQL is **multi-step and error-prone**.
Without LangGraph, you’d just “ask the LLM” and hope for the best. With LangGraph:

* You get a **structured pipeline** instead of a single fragile call.
* Failures can be retried or repaired (e.g., regenerate SQL if schema mismatch).
* You can **inject schema + sample data** at just the right stage.
* Results can be summarized differently depending on the query type (counts vs aggregations vs text searches).

This makes the whole system **far more reliable, interpretable, and extensible**.

