from pydantic import BaseModel


# -----------------------------
# AUTH
# -----------------------------
class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    role: str


# -----------------------------
# DEPLOYMENT
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
# REPORT
# -----------------------------
class DeploymentReport(BaseModel):
    application: str
    environment: str
    total: int
    success: int
    failed: int
