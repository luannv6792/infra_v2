from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    conn = psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        dbname=os.getenv("DATABASE_NAME"),
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT message FROM hello LIMIT 1")
    msg = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"message": msg}
