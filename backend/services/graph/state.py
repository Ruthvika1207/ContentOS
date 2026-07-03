from typing import TypedDict

class ContentState(TypedDict):
    workspace_id: str
    topic: str

    research: str
    competitor_report: str
    strategy: str
    seo_report: str
    content: str
    edited_content: str

    published_content: str
    
    critic_result: str
    needs_revision: bool

    retry_count: int
    max_retries: int


    