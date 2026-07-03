from services.rag.rag_chain import model


def run_critic_agent(strategy):

    prompt = f"""
You are a senior AI marketing reviewer.

Review the following marketing strategy.

Evaluate:

1. Is it complete?
2. Is it actionable?
3. Is it specific?
4. Does it have clear target audience?
5. Does it have measurable goals?

Respond with ONLY one word.

GOOD

or

BAD

Strategy:

{strategy}
"""

    response = model.generate_content(prompt)

    return response.text.strip().upper()