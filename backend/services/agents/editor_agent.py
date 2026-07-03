from services.rag.rag_chain import model


def run_editor_agent(content):

    prompt = f"""
You are a senior content editor.

Your task is to improve the content while preserving its meaning.

Content:

{content}

Improve:

1. Grammar
2. Readability
3. Professional tone
4. Brand consistency
5. Call-to-action
6. Formatting
7. Remove repetition

Do NOT rewrite from scratch.

Return the improved version only.
"""

    response = model.generate_content(
        prompt
    )

    return response.text