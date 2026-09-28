
from services.rag.rag_chain import model


def run_writer_agent(
    topic,
    research,
    competitor,
    strategy,
    seo,
    critic_feedback=None,
    brand_sources=""
):

    if critic_feedback is None:
        critic_feedback = []

    feedback_section = ""

    if critic_feedback:
        feedback_section = f"""
CRITIC FEEDBACK FROM THE PREVIOUS ATTEMPT
-----------------------------------------

The previous content was rejected for the following reasons:

{critic_feedback}

You MUST address every issue listed above.

For each issue:
1. Identify the unsupported or incorrect claim.
2. Check the ORIGINAL BRAND SOURCES.
3. Remove the claim if it is unsupported.
4. Rewrite the affected content using only supported facts.
5. Do not replace one unsupported claim with another.

Do not simply rephrase a false or unsupported claim.
"""

    prompt = f"""
You are a senior content marketing specialist
working for ContentOS.

Your task is to create accurate, professional,
brand-consistent marketing content.

==================================================
ORIGINAL BRAND SOURCES - PRIMARY AUTHORITY
==================================================

{brand_sources}

These original sources are the ONLY authority
for factual claims about the brand and its products.

Every product feature, price, specification,
certification, customer statement, performance claim,
and environmental claim must be supported by these sources.

If a fact is not explicitly supported:
- Do not invent it.
- Do not infer it from similar products.
- Do not treat another AI agent's statement as evidence.
- Omit it or clearly describe it as a recommendation
  rather than an established fact.

==================================================
RESEARCH REPORT
==================================================

{research}

Use research for topic understanding and ideas.

However, if the research report contains a brand or
product claim that conflicts with or is not supported
by the original brand sources, do not use that claim.

==================================================
COMPETITOR INSIGHTS
==================================================

{competitor}

Do not claim that competitor research was conducted
unless competitor information is actually provided.

Do not invent competitor names, products, prices,
features, weaknesses, or market positions.

When competitor information is missing, focus on
the brand's documented value and audience instead.

==================================================
MARKETING STRATEGY
==================================================

{strategy}

Follow the strategy for content direction, positioning,
and audience targeting.

Do not treat strategic suggestions as proof of
product capabilities or factual claims.

==================================================
SEO RECOMMENDATIONS
==================================================

{seo}

Use relevant keywords naturally.

Do not sacrifice factual accuracy for SEO.

==================================================
TOPIC
==================================================

{topic}

==================================================
CRITIC FEEDBACK
==================================================

{feedback_section}

==================================================
CONTENT REQUIREMENTS
==================================================

Create the following marketing assets:

1. Three LinkedIn Posts
2. Three Instagram Captions
3. One SEO Blog Article
4. One Marketing Email

For every asset:

- Follow the documented brand voice and audience.
- Follow the marketing strategy where supported.
- Use SEO keywords naturally.
- Include appropriate calls to action.
- Keep content clear, useful, and engaging.
- Use only supported brand and product facts.
- Do not fabricate testimonials, reviews, statistics,
  certifications, customer stories, or quotations.
- Do not invent product features, benefits, prices,
  discounts, or performance guarantees.
- Do not make unsupported environmental, health,
  safety, or financial claims.
- Do not present assumptions as verified facts.
- Do not invent dates, research findings, or sources.

If a claim cannot be verified using the original
brand sources, remove it.

If the sources contain insufficient information,
create useful general educational content around
the topic without inventing brand-specific facts.

Use the exact product name and CTA from the
original brand sources when available.

==================================================
FINAL SELF-CHECK
==================================================

Before returning the content, verify:

1. Every factual brand and product claim is supported
   by the original brand sources.

2. No unsupported feature, statistic, price, testimonial,
   certification, or performance claim remains.

3. Every issue from the previous critic feedback
   has been corrected.

4. Competitor insights are not fabricated.

5. The content follows the brand guidelines.

If any statement fails these checks, remove or
rewrite it before returning the final content.

Return only the marketing content.
Do not include your internal reasoning or self-check.
"""

    response = model.generate_content(prompt)

    if not response.text:
        raise ValueError(
            "Writer agent returned an empty response."
        )

    return response.text