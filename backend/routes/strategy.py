from fastapi import APIRouter
from pydantic import BaseModel

from services.agents.strategy_agent import (
    run_strategy_agent
)

router = APIRouter()

class StrategyRequest(BaseModel):

    workspace_id: str
    topic: str

@router.post("/strategy")
def strategy(
    request: StrategyRequest
):

    result = run_strategy_agent(
        request.workspace_id,
        request.topic
    )

    return {
        "strategy": result
    }