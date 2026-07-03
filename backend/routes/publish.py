from fastapi import APIRouter
from pydantic import BaseModel

from services.agents.publishing_agent import (
    run_publishing_agent
)

from services.campaign.campaign_service import (
    create_campaign
)

router = APIRouter()


class PublishRequest(BaseModel):

    user_id: str
    topic: str
    content: str


@router.post("/publish")
def publish(request: PublishRequest):

    published_content = run_publishing_agent(
        request.content
    )

    create_campaign(

        user_id=request.user_id,

        topic=request.topic,

        content=published_content,

        platform="All",

        status="Published"

    )

    return {

        "message": "Campaign published successfully",

        "published_content": published_content

    }