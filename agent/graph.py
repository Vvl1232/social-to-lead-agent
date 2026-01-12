from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.intent import detect_intent
from agent.tools import mock_lead_capture
from agent.rag import load_rag

# Load RAG once
vectorstore = load_rag()


def agent_node(state: AgentState):
    # Latest user message (dict)
    last_message = state["messages"][-1]
    user_text = last_message["content"]

    # -------------------------
    # Save user responses
    # -------------------------
    if state.get("last_question") == "name":
        state["name"] = user_text
        state["last_question"] = None

    elif state.get("last_question") == "email":
        state["email"] = user_text
        state["last_question"] = None

    elif state.get("last_question") == "platform":
        state["platform"] = user_text
        state["last_question"] = None

    # -------------------------
    # Intent Detection (lock after high-intent)
    # -------------------------
    if state.get("intent") != "high_intent":
        state["intent"] = detect_intent(last_message)

    intent = state["intent"]

    # -------------------------
    # PRODUCT / PRICING FLOW
    # -------------------------
    if intent == "product_inquiry":
        docs = vectorstore.similarity_search(user_text, k=2)
        response_text = "\n".join(doc.page_content for doc in docs)

        return {
            **state,
            "messages": state["messages"] + [
                {"role": "assistant", "content": response_text}
            ],
        }

    # -------------------------
    # HIGH-INTENT LEAD FLOW
    # -------------------------
    if intent == "high_intent":

        if state.get("lead_captured"):
            return {
                **state,
                "messages": state["messages"] + [
                    {
                        "role": "assistant",
                        "content": "Happy to help! Let me know if you need anything else 😊",
                    }
                ],
            }

        if state["name"] is None:
            return {
                **state,
                "last_question": "name",
                "messages": state["messages"] + [
                    {"role": "assistant", "content": "Great! May I have your name?"}
                ],
            }

        if state["email"] is None:
            return {
                **state,
                "last_question": "email",
                "messages": state["messages"] + [
                    {"role": "assistant", "content": "Thanks! Can you share your email?"}
                ],
            }

        if state["platform"] is None:
            return {
                **state,
                "last_question": "platform",
                "messages": state["messages"] + [
                    {
                        "role": "assistant",
                        "content": "Which platform do you create content on?",
                    }
                ],
            }

        # -------------------------
        # TOOL CALL (SAFE)
        # -------------------------
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"],
        )

        return {
            **state,
            "lead_captured": True,
            "messages": state["messages"] + [
                {
                    "role": "assistant",
                    "content": "You're all set! Our team will reach out soon.",
                }
            ],
        }

    # -------------------------
    # DEFAULT / GREETING
    # -------------------------
    return {
        **state,
        "messages": state["messages"] + [
            {"role": "assistant", "content": "Hello! How can I help you today?"}
        ],
    }


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    return graph.compile()