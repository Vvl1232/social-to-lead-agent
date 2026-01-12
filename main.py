import streamlit as st
from agent.graph import build_graph

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="AutoStream AI Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AutoStream AI Agent")
st.caption("Agentic AI Demo • Type 'exit' to reset")

# -------------------------
# Build Agent (once)
# -------------------------
@st.cache_resource
def load_agent():
    return build_graph()

app = load_agent()

# -------------------------
# Session State Init
# -------------------------
if "state" not in st.session_state:
    st.session_state.state = {
        "messages": [],
        "intent": "",
        "name": None,
        "email": None,
        "platform": None,
        "last_question": None,
        "lead_captured": False
    }

# -------------------------
# Display Chat History
# -------------------------
for msg in st.session_state.state["messages"]:
    if isinstance(msg, dict):
        role = msg.get("role", "assistant")
        content = msg.get("content", "")
    else:
        role = "user"
        content = msg

    with st.chat_message(role):
        st.write(content)

# -------------------------
# User Input
# -------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    if user_input.lower() == "exit":
        st.session_state.clear()
        st.rerun()


    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Update state
    st.session_state.state["messages"].append(user_input)

    # Invoke agent
    result = app.invoke(st.session_state.state)

    # Critical update
    st.session_state.state.update(result)

    # Get latest agent message
    agent_reply = result["messages"][-1]

    # Show agent message
    with st.chat_message("assistant"):
        st.write(agent_reply)