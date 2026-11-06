
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


def create_vector_store(
    embeddings: OllamaEmbeddings,
    persist_directory: str = "chroma_db",
) -> Chroma:
    return Chroma(
        collection_name="rag_documents",
        embedding_function=embeddings,
        persist_directory=persist_directory,
    )
