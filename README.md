# Social to Lead Agent – AutoStream

This project is built as part of the ServiceHive Machine Learning Intern assignment.

The goal of this project is to build an agentic AI system that converts social media conversations into qualified leads.

The agent is designed for a fictional SaaS product called **AutoStream**, which provides automated video editing tools for content creators.

---

## Features

- Intent detection (greeting, product inquiry, high intent)
- RAG-based product and pricing responses using a local knowledge base
- Multi-turn conversation state management
- Lead qualification and controlled tool execution
- Streamlit-based interactive UI

---

## Tech Stack

- Python 3.9+
- Streamlit
- LangChain
- LangGraph (for agent workflow and state management)
- FAISS (vector search)
- HuggingFace sentence embeddings

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vvl1232/social-to-lead-agent.git
cd social-to-lead-agent
```

2. Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```
streamlit run main.py
```

## Project Structure
```
social-to-lead-agent/
│
├── agent/
│   ├── graph.py              # LangGraph agent workflow
│   ├── rag.py                # RAG pipeline
│   ├── intent.py             # Intent detection logic
│   ├── tools.py              # Mock lead capture tool
│   ├── state.py              # Agent state definition
│   └── __init__.py
│
├── data/
│   └── knowledge_base.json   # Local product knowledge base
│
├── main.py                   # Streamlit entry point
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
└── .gitignore
```

## Architecture Explanation
```
This project uses LangGraph to manage the agent’s decision flow and maintain state across multiple conversation turns.
The agent state stores conversation history, detected intent, user details, and tool execution status.

Intent detection is implemented using simple rule-based logic to ensure predictable and controlled behavior.
When a user asks about pricing or features, the agent uses Retrieval-Augmented Generation (RAG) to retrieve information from a local JSON knowledge base. The data is embedded using HuggingFace embeddings and stored in a FAISS vector store.

When high intent is detected, the agent enters a lead qualification flow. The agent sequentially collects the user’s name, email, and creator platform. The mock lead capture tool is executed only after all required details are collected, ensuring safe tool usage.
```

## WhatsApp Integration (Concept)
```
This agent can be integrated with WhatsApp using a webhook-based architecture.

Incoming WhatsApp messages would be received via a webhook endpoint and passed to the agent backend.
The agent’s response would then be sent back to the user using the WhatsApp Business API.

The same agent logic and state management can be reused without modification.
```

## Demo Video Submited