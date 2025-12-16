from fastapi import FastAPI, HTTPException
from .schemas import DeploymentCreate, DeploymentToday
from .models import (
    get_application_id,
    get_environment_id,
    insert_deployment,
    get_today_deployments
)

app = FastAPI(
    title="Deploy Monitor Backend",
    version="1.0.0"
)

# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------
@app.get("/health")
def health():
    """
    Health check cho k8s / ingress
    """
    return {"status": "ok"}


# --------------------------------------------------
# CREATE DEPLOYMENT EVENT
# --------------------------------------------------
@app.post("/api/deployments")
def create_deployment(payload: DeploymentCreate):
    """
    Ghi nhận 1 lần deploy vào database.

    Flow:
    1. Resolve application name -> application_id
    2. Resolve environment name -> environment_id
    3. Insert deployment record
    """
    try:
        # 1. Resolve application
        app_id = get_application_id(payload.application)

        # 2. Resolve environment
        env_id = get_environment_id(payload.environment)

        # 3. Insert deployment
        insert_deployment(
            application_id=app_id,
            environment_id=env_id,
            status=payload.status
        )

        return {"message": "Deployment recorded"}

    except ValueError as e:
        # Lỗi dữ liệu nghiệp vụ (app/env không tồn tại)
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        # Lỗi hệ thống – KHÔNG NUỐT LỖI
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# GET TODAY DEPLOYMENTS (DASHBOARD)
# --------------------------------------------------
@app.get(
    "/api/deployments/today",
    response_model=list[DeploymentToday]
)
def deployments_today():
    """
    Trả về danh sách deploy trong ngày,
    lấy từ VIEW deployment_today
    """
    try:
        rows = get_today_deployments()

        return [
            {
                "application": r[0],
                "environment": r[1],
                "total": r[2]
            }
            for r in rows
        ]

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
