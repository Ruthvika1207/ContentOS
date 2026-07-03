from fastapi import APIRouter
from pydantic import BaseModel

from services.workflows.langgraph_workflow import (
    run_langgraph_workflow
)

router = APIRouter()

class WorkflowRequest(BaseModel):
    workspace_id: str
    topic: str

@router.post("/generate-package")
def generate_package(
    request: WorkflowRequest
):

    result = run_langgraph_workflow(
    request.workspace_id,
    request.topic
)

    return result