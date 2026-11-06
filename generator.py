
from langchain_ollama import ChatOllama


def generate_answer(question: str, context: str) -> str:
    llm = ChatOllama(
        model="qwen2.5:1.5b",
        temperature=0,
    )

    prompt = f"""
Answer the question using only the provided context.

If the context does not contain the answer, say you could not
find the answer in the provided documents.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content
