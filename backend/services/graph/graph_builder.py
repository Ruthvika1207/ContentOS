from langgraph.graph import StateGraph, END

from services.graph.state import ContentState

from services.agents.research_agent import (
    run_research_agent
)

from services.agents.strategy_agent import (
    run_strategy_agent
)

from services.agents.writer_agent import (
    run_writer_agent
)
from services.agents.critic_agent import run_critic_agent

from services.agents.competitor_agent import (
    run_competitor_agent
)

from services.agents.seo_agent import (
    run_seo_agent
)

from services.agents.editor_agent import (
    run_editor_agent
)

# -----------------------------
# Research Node
# -----------------------------


def research_node(state):

    print("\n========== Research Node ==========")

    result = run_research_agent(
        state["workspace_id"],
        state["topic"]
    )

    # Store the generated research report
    state["research"] = result["research_report"]

    # Store the original retrieved PDF text
    state["brand_sources"] = result["brand_sources"]

    print("Research report generated.")
    print("Original brand sources stored.")

    return state



def competitor_node(state):

    print("\n========== Competitor Agent ==========")

    report = run_competitor_agent(
        state["topic"]
    )

    state["competitor_report"] = report

    return state


# -----------------------------
# Strategy Node
# -----------------------------

def strategy_node(state):

    print("\n========== Strategy Node ==========")

    strategy = run_strategy_agent(
        state["research"],
        state["competitor_report"]
    )

    state["strategy"] = strategy

    if len(strategy) < 300:

        state["needs_revision"] = True

    else:

        state["needs_revision"] = False

    return state


def decide_next(state):

    result = state["critic_result"]

    if result["verdict"] == "GOOD":
        state["needs_revision"] = False
        return END

    state["retry_count"] += 1

    print(f"Retry Attempt: {state['retry_count']}")

    if state["retry_count"] >= state["max_retries"]:
        print("Maximum retries reached.")
        state["needs_revision"] = True
        return END

    return "writer"



def seo_node(state):

    print("\n========== SEO Agent ==========")

    seo = run_seo_agent(

        state["strategy"],

        state["topic"]

    )

    state["seo_report"] = seo

    return state


# -----------------------------
# Writer Node
# -----------------------------

def writer_node(state):

    print("\n========== Writer Node ==========")

    content = run_writer_agent(
        state["topic"],
        state["research"],
        state["competitor_report"],
        state["strategy"],
        state["seo_report"],
        state.get("critic_feedback", [])
    )

    state["content"] = content

    return state


def editor_node(state):

    print("\n========== Editor Agent ==========")

    edited = run_editor_agent(
        state["content"]
    )

    state["edited_content"] = edited

    return state




def critic_node(state):

    print("\n========== Critic Agent ==========")

    result = run_critic_agent(
        state["edited_content"],
        state.get("brand_sources", ""),
        state["topic"]
    )

    state["critic_result"] = result
    state["critic_feedback"] = result["issues"]

    state["needs_revision"] = (
        result["verdict"] != "GOOD"
    )

    print("Critic verdict:", result["verdict"])

    if result["issues"]:
        print("Critic feedback:", result["issues"])

    return state

# -----------------------------
# Build Graph
# -----------------------------

builder = StateGraph(ContentState)

builder.add_node(
    "research",
    research_node
)

builder.add_node(
    "competitor",
    competitor_node
)

builder.add_node(
    "strategy",
    strategy_node
)

builder.add_node(
    "seo",
    seo_node
)

builder.add_node(
    "editor",
    editor_node
)

builder.add_node(
    "critic",
    critic_node
)

builder.add_node(
    "writer",
    writer_node
)

builder.set_entry_point(
    "research"
)

builder.add_edge(
    "research",
    "competitor"
)

builder.add_edge(
    "competitor",
    "strategy"
)

builder.add_edge(
    "strategy",
    "seo"
)

builder.add_edge(
    "seo",
    "writer"
)

builder.add_edge(
    "writer",
    "editor"
)

builder.add_edge(
    "editor",
    "critic"
)



builder.add_conditional_edges(

    "critic",

    decide_next,

    {

        "writer": "writer",

        END: END

    }

)





graph = builder.compile()