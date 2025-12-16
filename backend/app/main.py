from fastapi import FastAPI, HTTPException
from .schemas import DeploymentCreate, DeploymentToday
from .models import (
    get_application_id,
    get_environment_id,
    insert_deployment,
    get_today_deployments
)

app = FastAPI(title="Deploy Monitor Backend")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/deployments")
def create_deployment(payload: DeploymentCreate):
    """
    API ghi nhận 1 lần deploy.
    """
    try:
        app_id = get_application_id(payload.application)
        env_id = get_environment_id(payload.environment)
        insert_deployment(app_id, env_id, payload.status)
        return {"message": "Deployment recorded"}
    except ValueError as e:
        # lỗi dữ liệu logic (application/env không tồn tại)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # lỗi hệ thống
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/api/deployments/today", response_model=list[DeploymentToday])
def deployments_today():
    """
    API trả deploy trong ngày (cho dashboard).
    """
    rows = get_today_deployments()
    return [
        {
            "application": r[0],
            "environment": r[1],
            "total": r[2]
        }
        for r in rows
    ]
