
from services.graph.graph_builder import graph


def run_langgraph_workflow(
    workspace_id,
    topic
):

    state = {
        "workspace_id": workspace_id,
        "topic": topic,

        "research": "",
        "brand_sources": "",  # ADDED

        "competitor_report": "",
        "strategy": "",
        "seo_report": "",

        "content": "",
        "edited_content": "",
        "published_content": "",

        "critic_result": {},
        "critic_feedback": [],

        "needs_revision": False,

        "retry_count": 0,
        "max_retries": 1
    }

    result = graph.invoke(state)

    return result