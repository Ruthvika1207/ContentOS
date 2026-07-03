from services.graph.graph_builder import graph


def run_langgraph_workflow(
    workspace_id,
    topic
):

    state = {

    "workspace_id": workspace_id,

    "topic": topic,

    "research": "",

    "strategy": "",

    "content": "",

    "critic_result": "",

    "needs_revision": False,

    "retry_count": 0,

    "max_retries": 2
}

    result = graph.invoke(
        state
    )

    return result