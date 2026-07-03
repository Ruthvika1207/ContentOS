from fastapi import APIRouter
from pydantic import BaseModel

from services.agents.research_agent import (
    run_research_agent
)

router = APIRouter()

class ResearchRequest(BaseModel):

    workspace_id: str
    topic: str

@router.post("/research")
def research(
    request: ResearchRequest
):

    result = run_research_agent(
        request.workspace_id,
        request.topic
    )

    return {
        "report": result
    }