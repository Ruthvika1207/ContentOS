from pydantic import BaseModel

class WorkspaceCreate(BaseModel):
    user_id: str
    name: str
    description: str