from services.rag.rag_chain import model


def run_critic_agent(content):

    prompt = f"""
You are a Senior Marketing Quality Reviewer.

Review the following generated marketing content.

==================================================
CONTENT
==================================================

{content}

Evaluate the content on:

1. Readability
2. Marketing effectiveness
3. SEO optimization
4. Call-to-Action
5. Brand consistency
6. Grammar
7. Professional tone

Internally give the content a score out of 10.

Decision Rules:

- Score >= 7 → GOOD
- Score < 7 → BAD

Be practical.

Do NOT reject content for small improvements.

Reject ONLY if the content is incomplete,
poorly written,
or unusable.

Return ONLY ONE WORD:

GOOD

or

BAD
"""

    response = model.generate_content(prompt)

    return response.text.strip().upper()