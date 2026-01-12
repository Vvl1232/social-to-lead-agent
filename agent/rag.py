import json
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def load_rag():
    with open("data/knowledge_base.json", "r") as f:
        data = json.load(f)

    documents = []
    for section, content in data.items():
        documents.append(
            Document(page_content=f"{section}: {content}")
        )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore