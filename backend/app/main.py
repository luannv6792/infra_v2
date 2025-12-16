from fastapi import FastAPI, HTTPException, Depends
from psycopg2.extras import RealDictCursor
from .db import get_connection
from .dependencies import get_current_user, require_admin
from .schemas import (
    LoginRequest,
    LoginResponse,
    DeploymentCreate,
    DeploymentToday,
    DeploymentReport,
)
from .models import (
    get_user_by_username,
    get_application_id,
    get_environment_id,
    insert_deployment,
    get_today_deployments,
)
from .auth import verify_password, create_access_token

app = FastAPI(title="Deploy Monitor Backend", version="1.3.0")


@app.get("/health")
def health():
    return {"status": "ok"}


# -----------------------------
# AUTH
# -----------------------------
@app.post("/api/auth/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    user = get_user_by_username(payload.username)
    if not user or not verify_password(
        payload.password, user["password_hash"]
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        {"username": user["username"], "role": user["role"]}
    )
    return {"access_token": token, "role": user["role"]}


# -----------------------------
# DEPLOYMENTS TODAY
# -----------------------------
@app.get(
    "/api/deployments/today",
    response_model=list[DeploymentToday],
)
def deployments_today(user=Depends(get_current_user)):
    rows = get_today_deployments()
    return [
        {"application": r[0], "environment": r[1], "total": r[2]}
        for r in rows
    ]


# -----------------------------
# ALERT TODAY (ADMIN ONLY)
# -----------------------------
@app.get("/api/alerts/today")
def alert_today(user=Depends(require_admin)):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT
                  COUNT(*) AS failed_count,
                  ARRAY_AGG(DISTINCT a.name) AS applications
                FROM deployment d
                JOIN application a ON d.application_id = a.id
                WHERE d.status = 'failed'
                  AND d.deploy_time >= date_trunc('day', now())
                """
            )
            row = cur.fetchone()

    failed_count = row["failed_count"] or 0
    return {
        "has_failed": failed_count > 0,
        "failed_count": failed_count,
        "applications": row["applications"] or [],
    }


# -----------------------------
# REPORTS (ADMIN ONLY)
# -----------------------------
@app.get("/api/reports/monthly", response_model=list[DeploymentReport])
def report_monthly(user=Depends(require_admin)):
    raise HTTPException(status_code=501, detail="Not implemented yet")


@app.get("/api/reports/yearly", response_model=list[DeploymentReport])
def report_yearly(user=Depends(require_admin)):
    raise HTTPException(status_code=501, detail="Not implemented yet")
