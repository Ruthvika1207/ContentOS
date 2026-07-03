from pydantic import BaseModel

class ChatRequest(BaseModel):
    workspace_id: str
    question: str