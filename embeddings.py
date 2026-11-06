
from langchain_ollama import OllamaEmbeddings


def create_embeddings() -> OllamaEmbeddings:
    return OllamaEmbeddings(
        model="nomic-embed-text:latest",
    )
