from services.agents.research_agent import (
    run_research_agent
)

from services.agents.strategy_agent import (
    run_strategy_agent
)

from services.agents.writer_agent import (
    run_writer_agent
)

def run_content_workflow(
    workspace_id,
    topic
):

    print("Running Research Agent...")

    research = run_research_agent(
        workspace_id,
        topic
    )

    print("Running Strategy Agent...")

    strategy = run_strategy_agent(
        research
    )

    print("Running Writer Agent...")

    content = run_writer_agent(
        strategy
    )

    return {
        "research": research,
        "strategy": strategy,
        "content": content
    }