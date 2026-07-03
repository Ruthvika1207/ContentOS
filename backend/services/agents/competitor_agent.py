from services.rag.rag_chain import model


def run_competitor_agent(topic):

    prompt = f"""
You are an experienced competitive intelligence analyst.

The business topic is:

{topic}

Perform competitor research.

Return the report in the following format.

# Top Competitors

# Their Strengths

# Their Weaknesses

# Pricing Strategy

# Marketing Strategy

# Social Media Presence

# Opportunities

# Threats

Keep the report practical and structured.
"""

    response = model.generate_content(
        prompt
    )

    return response.text