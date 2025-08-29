# AI CSV → SQL Agent (MCP + LangGraph + Mistral)

## Overview

This project is a **CSV question-answering agent** that allows users to upload a CSV file and ask questions in plain English. The agent automatically:

1. Converts natural language questions into SQL queries.
2. Executes SQL queries on the uploaded CSV.
3. Returns **concise natural language answers** instead of raw tables or dictionaries.

The app is structured using the **MCP (Model–Controller–Processor) pattern** for clean, modular code.

## Demo - 

Try it live on Hugging Face Spaces:  
<img width="1152" height="507" alt="image" src="https://github.com/user-attachments/assets/6bdd49a1-beb7-4ff5-b6b9-a7743260a0c2" />

<img width="1363" height="590" alt="image" src="https://github.com/user-attachments/assets/9072d2d7-8af7-44bf-82f2-b51d56528cfc" />
---

## Features

* Upload any CSV file.
* Ask questions in natural language.
* AI generates SQL queries and executes them.
* Results are returned as neat **plain English sentences**.
* Interactive and polished UI built with **Gradio**.
* LLM powered by **Mistral via OpenRouter API**.
* Workflow orchestrated using **LangGraph** for modular node-based execution.

---

## MCP Architecture

### **Processor (P)**

* Handles **data ingestion and formatting**.
* Loads CSV into an in-memory SQLite database.
* Formats output into HTML cards for the UI.

### **Model (M)**

* Handles **logic and computation**.
* Calls LLM to generate SQL queries from user questions.
* Executes SQL queries.
* Converts query results into **concise natural language answers**.

### **Controller (C)**

* **Orchestrates the workflow** between Processor and Model.
* Receives user questions and invokes Model & Processor methods.
* Returns final formatted results to the UI.

---

## How it Works

1. User uploads a CSV file → Processor loads it into SQLite.
2. User asks a question → Controller sends it to Model.
3. Model generates SQL using **Mistral LLM via OpenRouter**.
4. SQL is executed on the CSV → results returned to Model.
5. Model converts results into a **plain English answer**.
6. Controller passes the answer to Processor → formatted HTML card.
7. UI displays the result.

---

## Tech Stack

* **Python**
* **Gradio** for UI
* **SQLite** for in-memory CSV storage
* **LangGraph** for workflow orchestration
* **Mistral LLM via OpenRouter API** for natural language processing
* **Pandas** for CSV handling

---

## Screenshots

<!-- Add your screenshots here -->

![Screenshot 1](#)
![Screenshot 2](#)

---

## How to Run

1. Set your API key in environment variables:

   ```bash
   export OPENROUTER_API_KEY="YOUR_KEY"
   ```
2. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:

   ```bash
   python app.py
   ```
4. Open the provided Gradio link, upload your CSV, and start asking questions.

---

## Notes

* Works best with **short, clear questions**.
* Make sure column names in CSV are accurate for easier SQL generation.
* Fully modular code using **MCP** pattern: easy to extend or swap LLMs.
