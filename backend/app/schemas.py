from pydantic import BaseModel

class DeploymentCreate(BaseModel):
    application: str
    environment: str
    status: str  # success | failed (chưa validate gắt ở slice 1)

class DeploymentToday(BaseModel):
    application: str
    environment: str
    total: int
