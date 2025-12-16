from .db import get_connection

def get_application_id(name: str) -> int:
    """
    Lấy application.id từ tên.
    Nếu không tồn tại -> lỗi rõ ràng.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM application WHERE name = %s",
        (name,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        raise ValueError(f"Application '{name}' not found")

    return row[0]


def get_environment_id(name: str) -> int:
    """
    Lấy environment.id từ tên.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM environment WHERE name = %s",
        (name,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        raise ValueError(f"Environment '{name}' not found")

    return row[0]


def insert_deployment(application_id: int, environment_id: int, status: str):
    """
    Insert 1 deploy event.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO deployment(application_id, environment_id, deploy_time, status)
        VALUES (%s, %s, NOW(), %s)
        """,
        (application_id, environment_id, status)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_today_deployments():
    """
    Lấy dữ liệu tổng hợp trong ngày từ VIEW deployment_today.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT application, environment, total
        FROM deployment_today
        ORDER BY application, environment
        """
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows
