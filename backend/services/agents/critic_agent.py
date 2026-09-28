import json
import re

from services.rag.rag_chain import model


def run_critic_agent(content, brand_sources="", topic=""):

    prompt = f"""
You are the strict factual accuracy and brand compliance
reviewer for ContentOS.

Your primary responsibility is to prevent unsupported claims
from appearing in published marketing content.

The ORIGINAL BRAND SOURCES below are the authoritative
evidence for all brand and product facts.

The content must be checked against these sources directly.

==================================================
TOPIC
==================================================

{topic}

==================================================
ORIGINAL BRAND SOURCES
==================================================

{brand_sources}

==================================================
CONTENT TO REVIEW
==================================================

{content}

==================================================
REVIEW RULES
==================================================

A. FACTUAL ACCURACY

Check every factual claim about the brand, its products,
customers, pricing, performance, and environmental benefits.

A claim is supported only if the original brand sources
explicitly establish it.

Do not treat a claim as supported merely because:
- It sounds reasonable.
- It is common for similar products.
- It appears in the research report.
- Another AI agent has already written it.

Flag unsupported claims such as:
- Leak-proof or dishwasher-safe claims.
- Product performance or durability guarantees.
- Quantified environmental savings.
- Price comparisons or financial payback claims.
- Certifications, customer reviews, or testimonials.
- Invented product features or specifications.

These are examples, not an exhaustive list.

B. BRAND GUIDELINES

Check whether the content follows the brand's documented
voice, audience, messaging, and restrictions.

Flag unsupported environmental, health, safety,
or performance claims.

C. MISSING EVIDENCE

If the original brand sources are empty or do not support
a factual claim, do not assume that claim is true.

Flag the specific unsupported claim and explain
what evidence is missing.

Do not invent evidence or facts to justify a rejection.

D. CONTENT QUALITY

Check readability, grammar, relevance, SEO, and CTA.

Do not reject content for minor stylistic improvements.

==================================================
DECISION RULES
==================================================

Return BAD if:
- Any material product or brand claim is unsupported.
- The content contains fabricated testimonials,
  certifications, statistics, or performance claims.
- The content contradicts documented brand restrictions.
- The content is seriously misleading or unusable.

Return GOOD only if:
- Material factual claims are supported by the
  original brand sources.
- The content follows the supplied brand restrictions.
- No material factual or brand compliance issues remain.

When uncertain whether a material claim is supported,
return BAD and identify the claim.

==================================================
OUTPUT FORMAT
==================================================

Return ONLY valid JSON without Markdown code fences.

Use exactly this structure:

{{
    "verdict": "GOOD",
    "issues": []
}}

OR

{{
    "verdict": "BAD",
    "issues": [
        "Specific unsupported claim and why it is unsupported."
    ]
}}

For BAD, provide specific, actionable corrections
that the Writer agent can implement.

For GOOD, return an empty issues list.
"""

    response = model.generate_content(prompt)

    response_text = response.text.strip()

    # Remove Markdown code fences if Gemini includes them
    response_text = re.sub(
        r"^```(?:json)?\s*|\s*```$",
        "",
        response_text,
        flags=re.IGNORECASE
    ).strip()

    try:
        result = json.loads(response_text)

        verdict = result.get("verdict", "").strip().upper()
        issues = result.get("issues", [])

        if verdict not in ["GOOD", "BAD"]:
            raise ValueError("Invalid Critic verdict")

        if not isinstance(issues, list):
            raise ValueError("Critic issues must be a list")

        if not all(isinstance(issue, str) for issue in issues):
            raise ValueError("Every critic issue must be a string")

        # Never approve content if the critic reports issues
        if verdict == "GOOD" and issues:
            verdict = "BAD"

        # Never approve empty or missing brand evidence
        if not brand_sources or not brand_sources.strip():
            verdict = "BAD"
            issues = [
                "Original brand sources are missing. "
                "Verify the content against the uploaded "
                "brand knowledge before approval."
            ]

        if verdict == "GOOD":
            issues = []

        return {
            "verdict": verdict,
            "issues": issues
        }

    except (json.JSONDecodeError, ValueError, AttributeError):
        # Fail closed: invalid critic output must not
        # approve content.
        return {
            "verdict": "BAD",
            "issues": [
                "Critic response was invalid. Please regenerate "
                "and validate the content."
            ]
        }