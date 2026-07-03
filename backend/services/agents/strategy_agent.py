from services.rag.rag_chain import model


def run_strategy_agent(
    research_report,
    competitor_report
):

    prompt = f"""
You are a senior marketing strategist.

Your task is to create a complete marketing strategy.

Use BOTH:

1. Market Research
2. Competitor Analysis

Market Research:

{research_report}


Competitor Analysis:

{competitor_report}


Generate a structured strategy.

Include:

1. Target Audience

2. Brand Positioning

3. Content Pillars

4. Unique Selling Points

5. Competitive Advantages

6. 30-Day Content Calendar

7. Marketing Channels

8. Growth Opportunities

9. Recommended Actions

The strategy should clearly differentiate the brand from its competitors.
"""

    response = model.generate_content(
        prompt
    )

    return response.text