from fastapi import FastAPI, HTTPException, Depends
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
from .dependencies import require_admin, get_current_user

app = FastAPI(title="Deploy Monitor Backend", version="1.2.0")


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
# DEPLOYMENTS (DEV + ADMIN)
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


@app.post("/api/deployments")
def create_deployment(
    payload: DeploymentCreate, user=Depends(get_current_user)
):
    app_id = get_application_id(payload.application)
    env_id = get_environment_id(payload.environment)
    insert_deployment(app_id, env_id, payload.status)
    return {"message": "Deployment recorded"}


# -----------------------------
# REPORTS (ADMIN ONLY)
# -----------------------------
@app.get(
    "/api/reports/monthly",
    response_model=list[DeploymentReport],
)
def report_monthly(user=Depends(require_admin)):
    raise HTTPException(status_code=501, detail="Not wired to UI yet")


@app.get(
    "/api/reports/yearly",
    response_model=list[DeploymentReport],
)
def report_yearly(user=Depends(require_admin)):
    raise HTTPException(status_code=501, detail="Not wired to UI yet")
