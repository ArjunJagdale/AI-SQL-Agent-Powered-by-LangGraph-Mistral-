Here’s a concise README template for your project, explaining how it works and leaving space for demo screenshots:

---

# AI CSV → SQL Agent

A lightweight tool that allows you to **upload a CSV file, ask questions in plain English**, and get **answers in natural language**. The agent generates SQL internally to query the data but the user sees only readable English results.

---

## Demo - 

Try it live on Hugging Face Spaces:  
[AI CSV → SQL Agent](https://huggingface.co/spaces/ajnx014/Natural-Language-to-SQL-Agent)

<img width="1363" height="590" alt="image" src="https://github.com/user-attachments/assets/9072d2d7-8af7-44bf-82f2-b51d56528cfc" />

---

## Features

* Upload any CSV file and load it into an in-memory SQLite database.
* Ask questions in natural language about your data.
* The agent automatically generates SQL internally to fetch relevant results.
* SQL results are converted into **plain English answers** using an LLM.
* No technical knowledge of SQL is required.
* Clean, interactive Gradio interface for easy use.

---

## How It Works

1. **CSV Upload**

   * You upload a CSV file through the Gradio interface.
   * The file is loaded into an in-memory SQLite database (`data` table).

2. **Ask a Question**

   * Type a question in plain English, e.g., "What is the average score of students?"

3. **Internal SQL Generation**

   * A language model (Mistral via OpenRouter) converts the question into an appropriate SQL query.

4. **Execute SQL**

   * The query runs internally against the loaded CSV data.

5. **Generate Natural Language Answer**

   * The SQL results are converted into **human-readable English sentences** by the LLM.
   * The answer is displayed in the UI.

---

## Requirements

* Python 3.10+
* Packages: `gradio`, `pandas`, `sqlite3`, `httpx`, `langgraph`
* OpenRouter API key (or OpenAI API key) set in environment:

```bash
export OPENROUTER_API_KEY="YOUR_KEY_HERE"
```

---

## Usage

1. Clone this repository.
2. Install dependencies:

```bash
pip install gradio pandas httpx langgraph
```

3. Set your API key in environment variables.
4. Run the app:

```bash
python app.py
```

5. Open the provided Gradio URL in your browser.
6. Upload CSV → Ask a question → Get answers in plain English.

---

## Notes

* The agent works best with **short, clear questions**.
* If the question is ambiguous, try rephrasing.
* All SQL execution is **internal**, users see only the plain English results.

I can also draft a **minimal one-page version suitable for GitHub** with even simpler text if you want. Do you want me to do that?
