
from embeddings import create_embeddings
from vector_store import create_vector_store
from retriever import retrieve_documents
from generator import generate_answer


def ask_question(question: str) -> str:
    # 1. Connect to the existing vector store
    embeddings = create_embeddings()
    vector_store = create_vector_store(embeddings)

    # 2. Retrieve relevant document chunks
    documents = retrieve_documents(
        vector_store,
        question,
        k=4,
    )

    # 3. Combine the retrieved chunks into context
    context = "\n\n".join(
        document.page_content for document in documents
    )

    # 4. Generate the final answer using Qwen
    answer = generate_answer(question, context)

    return answer
