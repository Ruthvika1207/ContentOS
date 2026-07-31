from services.rag.rag_chain import model


def run_editor_agent(content):

    prompt = f"""
You are a Senior Marketing Editor.

Your responsibility is NOT to rewrite the content from scratch.

Instead, polish and improve it while preserving the original meaning.

Below is the generated marketing content.

==================================================
CONTENT
==================================================

{content}

==================================================
YOUR TASK
==================================================

Improve the following:

1. Grammar and spelling

2. Professional tone

3. Readability

4. Strong opening hook

5. Better storytelling

6. More engaging Call-to-Action

7. Better formatting using headings,
   bullet points and spacing where appropriate

8. Remove repetition

9. Improve flow between sections

10. Make the content more persuasive

11. Keep the brand voice consistent

12. Ensure each platform has an appropriate tone
    (LinkedIn, Instagram, Blog, Email)

IMPORTANT

• Do NOT change the core message.

• Do NOT invent new products.

• Keep factual information unchanged.

• Make the content feel polished,
  professional and publication-ready.

Return ONLY the improved content.
"""

    response = model.generate_content(prompt)

    return response.text