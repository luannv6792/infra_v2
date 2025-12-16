from datetime import date
from fastapi import FastAPI, HTTPException, Query

from .schemas import (
    DeploymentCreate,
    DeploymentToday,
    DeploymentReport
)
from .models import (
    get_application_id,
    get_environment_id,
    insert_deployment,
    get_today_deployments,
    get_monthly_report,
    get_yearly_report
)

app = FastAPI(
    title="Deploy Monitor Backend",
    version="1.1.0"
)


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# --------------------------------------------------
# SLICE 1 – CREATE DEPLOYMENT
# --------------------------------------------------
@app.post("/api/deployments")
def create_deployment(payload: DeploymentCreate):
    try:
        app_id = get_application_id(payload.application)
        env_id = get_environment_id(payload.environment)

        insert_deployment(
            application_id=app_id,
            environment_id=env_id,
            status=payload.status
        )

        return {"message": "Deployment recorded"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# SLICE 1 – TODAY DASHBOARD
# --------------------------------------------------
@app.get(
    "/api/deployments/today",
    response_model=list[DeploymentToday]
)
def deployments_today():
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


# --------------------------------------------------
# SLICE 2 – MONTHLY REPORT
# --------------------------------------------------
@app.get(
    "/api/reports/monthly",
    response_model=list[DeploymentReport]
)
def report_monthly(
    month: date = Query(..., description="Format: YYYY-MM-01")
):
    try:
        return get_monthly_report(month)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


# --------------------------------------------------
# SLICE 2 – YEARLY REPORT
# --------------------------------------------------
@app.get(
    "/api/reports/yearly",
    response_model=list[DeploymentReport]
)
def report_yearly(
    year: int = Query(..., ge=2000, le=2100)
):
    try:
        return get_yearly_report(year)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
