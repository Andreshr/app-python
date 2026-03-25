from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/user")
def get_user(name: str):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # ❌ VULNERABLE: input HTTP → SQL sin sanitizar
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor.execute(query)

    return {"ok": True}