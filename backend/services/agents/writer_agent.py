from services.rag.rag_chain import model


def run_writer_agent(

    topic,

    research,

    competitor,

    strategy,

    seo

):

    prompt = f"""
You are a senior content marketing specialist.

Use ALL the information below to create high-quality marketing assets.

Research Report
----------------
{research}

Competitor Insights
----------------
{competitor}

Marketing Strategy
----------------
{strategy}

SEO Recommendations
----------------
{seo}

Topic
----------------
{topic}

Create:

1. 3 LinkedIn Posts

2. 3 Instagram Captions

3. SEO Blog Article

4. Marketing Email

Requirements:

• Follow the strategy.

• Differentiate from competitors.

• Include SEO naturally.

• Keep the brand voice consistent.

• Use research insights.

• Include strong CTAs.

Return only the content.
"""

    response = model.generate_content(
        prompt
    )

    return response.text