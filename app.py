from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    # Leer variables sensibles desde el entorno
    db_password = os.getenv("DB_PASSWORD", "not-set")
    api_key = os.getenv("API_KEY", "not-set")

    return {
        "message": "Hello from FastAPI!",
        "db_password": db_password,
        "api_key": api_key
    }
