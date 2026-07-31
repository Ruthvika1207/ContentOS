from services.rag.rag_chain import model


def run_strategy_agent(
    research_report,
    competitor_report
):

    prompt = f"""
You are a Senior Marketing Strategist.

Your job is to create a practical, actionable marketing strategy.

The Market Research Report already contains insights from the company's Brand Brain
including its mission, vision, products, audience, brand voice and business goals.

Also use the Competitor Analysis to differentiate the company.

==============================
MARKET RESEARCH
==============================

{research_report}

==============================
COMPETITOR ANALYSIS
==============================

{competitor_report}

Create a professional marketing strategy with the following sections:

1. Executive Summary

2. Target Audience
   - Primary audience
   - Secondary audience
   - Customer pain points

3. Brand Positioning
   - Positioning statement
   - Value proposition

4. Unique Selling Proposition (USP)

5. Content Pillars
   - Educational
   - Promotional
   - Community
   - Thought Leadership

6. Marketing Channels
   - LinkedIn
   - Instagram
   - Email
   - Blog
   - YouTube (if relevant)

7. Competitive Advantages

8. 30-Day Content Plan

9. Growth Opportunities

10. Recommended Next Steps

Requirements:

- Align the strategy with the brand identity from the research.
- Differentiate from competitors.
- Keep recommendations realistic and actionable.
- Explain WHY each recommendation is made.
- Return only the strategy.
"""

    response = model.generate_content(prompt)

    return response.text