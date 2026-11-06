
from langchain_chroma import Chroma


def retrieve_documents(
    vector_store: Chroma,
    question: str,
    k: int = 4,
) -> list:
    results = vector_store.similarity_search(
        question,
        k=k,
    )

    return results
