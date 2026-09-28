
from typing import TypedDict, Any


class ContentState(TypedDict, total=False):
    workspace_id: str
    topic: str

    research: str
    brand_sources: str

    competitor_report: str
    strategy: str
    seo_report: str

    content: str
    edited_content: str
    published_content: str

    critic_result: dict[str, Any]
    critic_feedback: list[str]

    needs_revision: bool

    retry_count: int
    max_retries: int