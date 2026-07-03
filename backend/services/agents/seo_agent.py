from services.rag.rag_chain import model


def run_seo_agent(
    strategy,
    topic
):

    prompt = f"""
You are an expert SEO strategist.

Business Topic:

{topic}

Marketing Strategy:

{strategy}

Generate:

1. Primary Keyword

2. Secondary Keywords

3. SEO Title

4. Meta Description

5. URL Slug

6. Suggested Hashtags

7. Call-To-Action Keywords

8. Internal Linking Ideas

Return everything in a structured format.
"""

    response = model.generate_content(
        prompt
    )

    return response.text