# Social to Lead Agent

A sophisticated AI agent designed to convert social media interactions into qualified leads using advanced natural language processing and graph-based reasoning.

## Features

- **Intent Classification**: Automatically classify user intents from social media messages
- **RAG System**: Retrieve and generate responses using knowledge base
- **Graph-based Reasoning**: Model relationships and conversations
- **Lead Qualification**: Identify and qualify potential leads
- **Tool Integration**: Connect with various business tools

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vvl1232/social-to-lead-agent.git
cd social-to-lead-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run main.py
```

## Project Structure

```
social-to-lead-agent/
│
├── agent/
│   ├── graph.py              # Graph-based reasoning
│   ├── rag.py                # Retrieval-Augmented Generation
│   ├── intent.py             # Intent classification
│   ├── tools.py              # Tool integrations
│   ├── state.py              # State management
│   └── __init__.py
│
├── data/
│   └── knowledge_base.json   # Knowledge base data
│
├── main.py                   # Streamlit entry point
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
└── demo_video.mp4            # Demo video
```

## Demo

Watch the demo video: [demo_video.mp4](demo_video.mp4)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
