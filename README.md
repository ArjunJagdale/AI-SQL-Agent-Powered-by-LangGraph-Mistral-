# 📊 AI CSV Q&A Agent

An interactive Gradio app that lets you **ask natural language questions about your CSV files**.  
Upload a dataset, type your question, and get a **concise, human-readable answer** powered by **Pandas + LLMs (Mistral via OpenRouter)**.  

---

## 🚀 Features
- 📁 **Upload any CSV** and query it in plain English.  
- 🔍 **Direct lookup with Pandas** for exact matches (fast + accurate).  
- 🤖 **LLM-powered answers** when lookup is not enough.  
- 🎯 **Clean, natural responses** (no SQL, no verbose filler).  
- 🖥️ **Gradio interface** – simple and intuitive.  

---

## 🛠️ Tech Stack
- **[Gradio](https://www.gradio.app/):** UI framework for interaction.  
- **[Pandas](https://pandas.pydata.org/):** Data loading & direct search.  
- **[OpenRouter](https://openrouter.ai/):** API gateway for LLMs.  
- **[Mistral 24B Instruct](https://mistral.ai/):** The reasoning model answering your questions.  

---

## ⚙️ Setup & Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/ArjunJagdale/ai-csv-qa-agent.git
   cd ai-csv-qa-agent
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your **OpenRouter API Key** (in Hugging Face Spaces, set this as a secret named `OPENAI_API_KEY`):

   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

4. Run the app:

   ```bash
   python app.py
   ```

5. Open in browser → `http://127.0.0.1:7860`

---

## 📖 Usage

1. Upload your CSV file.
2. Ask a question in plain English (e.g., *"What is the college of Arjun Jagdale?"*).
3. The agent:

   * Checks for **direct matches** in your dataset.
   * If found → returns neat, formatted results.
   * If not → queries the LLM with dataset context.

Example:

**Input question:**

```
What is the college of Arjun Jagdale?
```

**Answer:**

```
📌 Results
- **Name**: Arjun Jagdale, **College**: Sinhgad Institute of Technology and Science (SITS) Pune, [Link](https://gfgcdn.com/tu/TK5/)
```

---

## 📂 Example CSV

| Name          | College                                                 | Profile URL                                                    |
| ------------- | ------------------------------------------------------- | -------------------------------------------------------------- |
| Arjun Jagdale | Sinhgad Institute of Technology and Science (SITS) Pune | [https://gfgcdn.com/tu/TK5/](https://gfgcdn.com/tu/TK5/)       |
| John Doe      | MIT                                                     | [https://example.com/johndoe](https://example.com/johndoe)     |
| Jane Smith    | Stanford University                                     | [https://example.com/janesmith](https://example.com/janesmith) |

---

## ✅ Roadmap

* [ ] Add support for **multi-CSV datasets**.
* [ ] Enable **filtering & sorting** options in UI.
* [ ] Support larger datasets with **chunked LLM context**.
* [ ] Add **export to CSV/JSON** for answers.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and create a PR.

---

## 📜 License

MIT License © 2025 Your Name

---

## 🙏 Acknowledgements

* [OpenRouter](https://openrouter.ai/) for API access to multiple LLMs.
* [Mistral](https://mistral.ai/) for powerful open models.
* [Gradio](https://www.gradio.app/) for simple UIs in Python.


Would you like me to also add a **demo screenshot/gif** section in the README so users immediately see how the app looks before running it?
```
