# app.py
from fastapi import FastAPI, Body
import sqlite3
import google.generativeai as genai
import os

# 🔹 Configure Gemini
genai.configure(api_key="AIzaSyDzhWHI8hGb2gTgfXeDeK4dnK9_RNp8Xpo")
model = genai.GenerativeModel("gemini-1.5-flash")

# 🔹 SQLite Schema (for Gemini prompt)
DB_SCHEMA = """
customers(customer_id, name, email)
accounts(account_id, customer_id, balance, account_type)
transactions(txn_id, account_id, amount, txn_type, txn_date)
"""

app = FastAPI()

# Convert NL → SQL using Gemini
def nl_to_sql(query: str) -> str:
    prompt = f"""
    You are an expert SQLite SQL generator for banking data.
    Convert the following natural language query into a valid SQLite SQL statement.

    Database schema:
    {DB_SCHEMA}

    User query: "{query}"

    Rules:
    - Output only raw SQL (no markdown, no explanation, no code fences).
    - If ambiguous, ask a clarifying question instead of guessing.
    - Use correct JOINs where needed.
    """
    response = model.generate_content(prompt)
    sql = response.text.strip()

    # 🔹 Remove accidental markdown/code fences
    if sql.startswith("```"):
        sql = sql.strip("`").replace("sql", "", 1).strip()
    return sql

# Execute SQL safely
def execute_sql(sql: str):
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        cols = [desc[0] for desc in cur.description] if cur.description else []
        conn.close()
        return {"columns": cols, "rows": rows}
    except Exception as e:
        conn.close()
        return {"error": str(e)}

@app.post("/query")
def query_nl(user_input: str = Body(..., embed=True)):
    sql = nl_to_sql(user_input)
    if sql.lower().startswith("select"):
        result = execute_sql(sql)
        return {"sql": sql, "result": result}
    else:
        # If Gemini asks a clarifying question
        return {"clarification": sql}
