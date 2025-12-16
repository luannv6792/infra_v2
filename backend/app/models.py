from datetime import date
from psycopg2.extras import RealDictCursor
from .db import get_connection


# -------------------------------------------------
# LOOKUP HELPERS (SLICE 1)
# -------------------------------------------------
def get_application_id(name: str) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM application WHERE name = %s",
                (name,)
            )
            row = cur.fetchone()
            if not row:
                raise ValueError(f"Application '{name}' not found")
            return row[0]


def get_environment_id(name: str) -> int:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM environment WHERE name = %s",
                (name,)
            )
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
                (application_id, environment_id, status)
            )
        conn.commit()


def get_today_deployments():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT application, environment, total
                FROM deployment_today
                """
            )
            return cur.fetchall()


# -------------------------------------------------
# REPORT QUERIES (SLICE 2)
# -------------------------------------------------
def get_monthly_report(month: date):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT
                  a.name AS application,
                  e.name AS environment,
                  COUNT(*) AS total,
                  COUNT(*) FILTER (WHERE d.status = 'success') AS success,
                  COUNT(*) FILTER (WHERE d.status = 'failed')  AS failed
                FROM deployment d
                JOIN application a ON d.application_id = a.id
                JOIN environment e ON d.environment_id = e.id
                WHERE d.deploy_time >= date_trunc('month', %s::date)
                  AND d.deploy_time <  date_trunc('month', %s::date) + interval '1 month'
                GROUP BY a.name, e.name
                ORDER BY total DESC
                """,
                (month, month)
            )
            return cur.fetchall()


def get_yearly_report(year: int):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT
                  a.name AS application,
                  e.name AS environment,
                  COUNT(*) AS total,
                  COUNT(*) FILTER (WHERE d.status = 'success') AS success,
                  COUNT(*) FILTER (WHERE d.status = 'failed')  AS failed
                FROM deployment d
                JOIN application a ON d.application_id = a.id
                JOIN environment e ON d.environment_id = e.id
                WHERE EXTRACT(YEAR FROM d.deploy_time) = %s
                GROUP BY a.name, e.name
                ORDER BY total DESC
                """,
                (year,)
            )
            return cur.fetchall()
