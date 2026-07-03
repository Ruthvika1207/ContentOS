from services.rag.retriever import retrieve_context
from services.rag.rag_chain import model

def run_research_agent(
    workspace_id,
    topic
):

    context = retrieve_context(
        workspace_id,
        topic
    )

    prompt = f"""
You are a market research analyst.

Use the provided brand knowledge and
generate a research report.

Brand Knowledge:
{context}

Research Topic:
{topic}

Generate:

1. Market Overview
2. Competitor Insights
3. Opportunities
4. Recommendations

Return a professional report.
"""

    response = model.generate_content(
        prompt
    )

    return response.text