import psycopg2
import os

def get_connection():
    """
    Tạo kết nối PostgreSQL.
    Mỗi request dùng 1 connection ngắn gọn (đủ cho slice 1).
    Sau này có thể thay bằng pool.
    """
    return psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        dbname=os.getenv("DATABASE_NAME"),
        port=5432
    )
