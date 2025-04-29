from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI Server Running"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            host="postgres",
            database=os.getenv("POSTGRES_DB", "crypto_db"),
            user=os.getenv("POSTGRES_USER", "user"),
            password=os.getenv("POSTGRES_PASSWORD", "password")
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return {"database": "Connected"}
    except Exception as e:
        return {"error": str(e)}
