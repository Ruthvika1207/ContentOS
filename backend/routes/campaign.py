from fastapi import APIRouter

from services.campaign.campaign_service import (
    get_campaigns,
    get_campaign,
    delete_campaign
)

router = APIRouter()


@router.get("/campaigns/{user_id}")
def campaigns(user_id: str):

    return get_campaigns(user_id)


@router.get("/campaign/{campaign_id}")
def campaign(campaign_id: str):

    return get_campaign(campaign_id)


@router.delete("/campaign/{campaign_id}")
def remove_campaign(campaign_id: str):

    delete_campaign(campaign_id)

    return {

        "message": "Campaign deleted successfully"

    }