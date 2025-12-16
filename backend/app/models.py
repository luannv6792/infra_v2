from psycopg2.extras import RealDictCursor
from .db import get_connection


# -----------------------------
# AUTH
# -----------------------------
def get_user_by_username(username: str):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT username, password_hash, role FROM users WHERE username = %s",
                (username,),
            )
            return cur.fetchone()


# -----------------------------
# DEPLOYMENT LOGIC (GIỮ NGUYÊN)
# -----------------------------
def get_application_id(name: str) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM application WHERE name = %s", (name,))
            row = cur.fetchone()
            if not row:
                raise ValueError(f"Application '{name}' not found")
            return row[0]


def get_environment_id(name: str) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM environment WHERE name = %s", (name,))
            row = cur.fetchone()
            if not row:
                raise ValueError(f"Environment '{name}' not found")
            return row[0]


def insert_deployment(application_id: int, environment_id: int, status: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO deployment(application_id, environment_id, deploy_time, status)
                VALUES (%s, %s, NOW(), %s)
                """,
                (application_id, environment_id, status),
            )
        conn.commit()


def get_today_deployments():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT application, environment, total FROM deployment_today"
            )
            return cur.fetchall()
