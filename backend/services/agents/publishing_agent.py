from services.rag.rag_chain import model


def run_publishing_agent(content):

    prompt = f"""
You are an AI Publishing Manager.

Convert the following content into platform-specific formats.

Content:
{content}

Generate:

1. LinkedIn Post
2. Instagram Caption
3. Twitter/X Post

Return each under a separate heading.
"""

    response = model.generate_content(prompt)

    return response.text