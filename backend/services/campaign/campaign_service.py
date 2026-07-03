from services.supabase_client import supabase


def create_campaign(
    user_id,
    topic,
    content,
    platform="All",
    status="Published"
):

    response = supabase.table(
        "campaigns"
    ).insert(
        {
            "user_id": user_id,
            "topic": topic,
            "content": content,
            "platform": platform,
            "status": status
        }
    ).execute()

    return response.data


def get_campaigns(user_id):

    response = supabase.table(
        "campaigns"
    ).select("*").eq(
        "user_id",
        user_id
    ).order(
        "created_at",
        desc=True
    ).execute()

    return response.data


def get_campaign(campaign_id):

    response = supabase.table(
        "campaigns"
    ).select("*").eq(
        "id",
        campaign_id
    ).single().execute()

    return response.data


def delete_campaign(campaign_id):

    response = supabase.table(
        "campaigns"
    ).delete().eq(
        "id",
        campaign_id
    ).execute()

    return response.data