from pydantic import BaseModel


# -----------------------------
# SLICE 1 – CREATE DEPLOYMENT
# -----------------------------
class DeploymentCreate(BaseModel):
    application: str
    environment: str
    status: str


class DeploymentToday(BaseModel):
    application: str
    environment: str
    total: int


# -----------------------------
# SLICE 2 – REPORT
# -----------------------------
class DeploymentReport(BaseModel):
    application: str
    environment: str
    total: int
    success: int
    failed: int
