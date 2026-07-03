from services.rag.rag_chain import model


def run_writer_agent(
    strategy,
    seo_report
):

    prompt = f"""
You are an expert marketing content writer.

Your task is to create high-quality marketing content.

Use BOTH:

1. Marketing Strategy

2. SEO Recommendations

------------------------------------------------

Marketing Strategy:

{strategy}

------------------------------------------------

SEO Recommendations:

{seo_report}

------------------------------------------------

Generate:

1. Three LinkedIn Posts

2. Three Instagram Captions

3. One SEO Optimized Blog Article

4. One Marketing Email

Requirements:

- Follow the marketing strategy.
- Naturally include the primary and secondary keywords.
- Use the suggested hashtags where appropriate.
- Maintain a consistent brand voice.
- Include strong call-to-actions.
- Make the blog SEO-friendly with headings.
"""

    response = model.generate_content(
        prompt
    )

    return response.text