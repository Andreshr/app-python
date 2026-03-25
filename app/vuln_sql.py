import sqlite3

def get_user(username: str):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # ❌ VULNERABLE: SQL construido con input del usuario
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()