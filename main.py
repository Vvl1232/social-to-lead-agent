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
        "messages": [],           # always store dict messages
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
    role = msg["role"]
    content = msg["content"]

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

    # ---- User message ----
    user_msg = {"role": "user", "content": user_input}
    st.session_state.state["messages"].append(user_msg)

    with st.chat_message("user"):
        st.write(user_input)

    # ---- Agent invoke ----
    result = app.invoke(st.session_state.state)

    # ---- Update global state ----
    st.session_state.state.update(result)

    # ---- Agent message ----
    agent_msg = result["messages"][-1]

    with st.chat_message("assistant"):
        st.write(agent_msg["content"])