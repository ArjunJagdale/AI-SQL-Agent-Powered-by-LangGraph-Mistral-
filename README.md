# 🔍 AI SQL Agent (LangGraph + Mistral)

An interactive agent built using **LangGraph**, powered by the **Mistral-3.2-24B** model via OpenRouter. This tool takes a user-uploaded CSV and answers natural language questions by generating and executing SQL queries — all within a few seconds.

> 🚀 Built for fast querying, natural interaction, and learning how AI can interact with structured data.

---

## 📌 Features

- Upload any CSV file 📁  
- Ask questions in plain English 🤖  
- Agent translates query to SQL (via LLM) 🔍  
- Executes query on in-memory SQLite 🧠  
- Displays clean, tabular answers 📊  
- Fully powered by [LangGraph](https://www.langchain.com/langgraph) for agentic behavior!

---

## 🧠 How It Works

### 1. Perceive
The user uploads a CSV file, which is loaded into an in-memory SQLite database.

### 2. Decide
LangGraph uses a stateful graph to:
- Analyze the database schema
- Extract sample rows
- Generate an SQL query using the Mistral model (via OpenRouter)

### 3. Act
The SQL is executed safely using `pandas.read_sql()`.

### 4. Adapt
Results are converted into readable markdown and shown to the user.

---

## 🧰 Tech Stack

| Component       | Purpose                         |
|----------------|----------------------------------|
| **LangGraph**  | Agent graph structure / state mgmt |
| **Mistral 3.2**| LLM that generates SQL            |
| **Gradio**     | UI for user interaction           |
| **SQLite**     | In-memory database from CSV       |
| **Pandas**     | CSV and SQL data manipulation     |
| **OpenRouter API** | LLM access with free-tier tokens |

---

## 🖼️ Demo Video
https://github.com/user-attachments/assets/7a0cc5e1-0f1a-47c3-ac18-2464efd915c5

---

## 💡 Example Use Case

Upload a CSV like this:

| Name | Institute Name                        |
|--------------------|----------------------------------------|
| Arjun Jagdale      | Sinhgad Institute of Technology and Science |

Then ask:
> *"Who is the Campus Mantri from BIT Patna?"*

The app will:
- Generate a SQL query
- Execute it on the dataset
- Show the matching row(s)

---

## 🔐 API Key Setup

Add your OpenRouter API key in your Hugging Face Space Secrets:

```

Name: OPENAI\_API\_KEY
Value: sk-xxx...your key

````

---

## 📦 Installation (for local dev)

```bash
pip install -r requirements.txt
````

> **requirements.txt**

```
gradio
langchain
langgraph
langchain-openai
httpx
pandas
sqlite-utils
```

---

## 🏁 Run Locally

```bash
python app.py
```

Or deploy to Hugging Face Spaces!

---

## 📘 Credits

* Built by Arjun Jagdale
* Using Open Source: LangGraph, Mistral, Gradio, SQLite

---

## 📄 License

MIT License
