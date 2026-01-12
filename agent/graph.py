from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.intent_classifier import detect_intent
from agent.tools import mock_lead_capture
from agent.rag import load_rag

vectorstore = load_rag()


def agent_node(state: AgentState):
    user_input = state["messages"][-1]

    #Save user response based on last question
    if state.get("last_question") == "name":
        state["name"] = user_input
        state["last_question"] = None

    elif state.get("last_question") == "email":
        state["email"] = user_input
        state["last_question"] = None

    elif state.get("last_question") == "platform":
        state["platform"] = user_input
        state["last_question"] = None

    #Lock intent after high-intent
    if state["intent"] != "high_intent":
        state["intent"] = detect_intent(user_input)

    intent = state["intent"]

    #PRODUCT INQUIRY
    if intent == "product_inquiry":
        docs = vectorstore.similarity_search(user_input, k=2)
        response = "\n".join([doc.page_content for doc in docs])
        return {
            **state,
            "messages": state["messages"] + [response],
        }

    #HIGH-INTENT LEAD FLOW
    if intent == "high_intent":

        if state.get("lead_captured"):
            return {
                **state,
                "messages": state["messages"]
                + ["Happy to help! Let me know if you need anything else 😊"],
            }

        if state["name"] is None:
            return {
                **state,
                "messages": state["messages"] + ["Great! May I have your name?"],
                "last_question": "name",
            }

        if state["email"] is None:
            return {
                **state,
                "messages": state["messages"] + ["Thanks! Can you share your email?"],
                "last_question": "email",
            }

        if state["platform"] is None:
            return {
                **state,
                "messages": state["messages"] + ["Which platform do you create content on?"],
                "last_question": "platform",
            }

        #TOOL CALL
        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )

        return {
            **state,
            "lead_captured": True,
            "messages": state["messages"]
            + ["You're all set! Our team will reach out soon."],
        }

    #DEFAULT
    return {
        **state,
        "messages": state["messages"] + ["Hello! How can I help you today?"],
    }


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    return graph.compile()