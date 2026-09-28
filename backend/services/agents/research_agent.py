
from services.rag.retriever import retrieve_context
from services.rag.rag_chain import model


def run_research_agent(workspace_id, topic):

    # Step 1: Retrieve relevant brand documents
    docs = retrieve_context(
        workspace_id,
        topic
    )

    # Step 2: Extract actual text from retrieved documents
    if isinstance(docs, str):
        context = docs
    else:
        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

    # Step 3: Handle empty retrieval
    if not context.strip():
        context = "No relevant brand knowledge was retrieved."

    # Step 4: Generate grounded research
    prompt = f"""
You are a market research analyst for a content marketing platform.

Use the provided brand knowledge as the source of truth
for all facts about the brand and its products.

BRAND KNOWLEDGE:
{context}

RESEARCH TOPIC:
{topic}

INSTRUCTIONS:

1. Separate facts from assumptions and recommendations.

2. Do not invent product features, prices, certifications,
   customer reviews, testimonials, or performance claims.

3. Do not claim competitor research has been performed
   unless competitor information is provided.

4. If information is missing, explicitly state
   "Not available in the provided brand knowledge."

5. You may provide general marketing recommendations,
   but clearly label them as recommendations or inferences,
   not verified facts.

Generate the following sections:

1. Brand and Product Overview
2. Target Audience
3. Available Market and Competitor Information
4. Potential Opportunities
5. Recommendations

For each factual claim about the brand or product,
use only information supported by the provided context.

Return a professional, structured report.
"""

    response = model.generate_content(prompt)

    return {
    "research_report": response.text,
    "brand_sources": context
}