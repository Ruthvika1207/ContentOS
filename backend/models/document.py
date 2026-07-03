from pydantic import BaseModel

class DocumentCreate(BaseModel):
    workspace_id: str
    content: str