from fastapi import APIRouter
from pydantic import BaseModel

from services.agents.writer_agent import (
    run_writer_agent
)

router = APIRouter()

class WriterRequest(BaseModel):

    workspace_id: str
    topic: str

@router.post("/writer")
def writer(
    request: WriterRequest
):

    result = run_writer_agent(
        request.workspace_id,
        request.topic
    )

    return {
        "content": result
    }