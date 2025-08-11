# SQL-Assistant

A Streamlit app that lets you query SQLite (student.db) or MySQL databases in natural language using LangChain and a local Ollama LLM.

## Features

- 💬 Chat interface to your database
- 🗃 Supports SQLite and MySQL
- 🤖 Powered by LangChain’s SQL Agent
- ⚡ Uses Ollama’s local LLM (llama3.1)

## Setup

```bash
pip install -r requirements.txt
ollama pull llama3.1
ollama serve
streamlit run app.py
```

##SQLite Sample DB

```bash
python create_student_db.py
```
This will create student.db with sample student data.
Place student.db in the same folder as app.py.

## MySQL
Select MySQL in the sidebar and provide:

- Host
- User
- Password
- Database name

