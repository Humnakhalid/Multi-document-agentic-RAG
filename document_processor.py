
from pathlib import Path

from ingestion import load_document
from chunking import split_text
from embeddings import create_embeddings
from vector_store import create_vector_store


def process_document(file_path: str) -> int:
    # 1. Load text from the document
    text = load_document(file_path)

    if not text.strip():
        raise ValueError("No text could be extracted from the document.")

    # 2. Split the text into chunks
    chunks = split_text(text)

    # 3. Create the embedding model and vector store
    embeddings = create_embeddings()
    vector_store = create_vector_store(embeddings)

    # 4. Identify the source document
    source = Path(file_path).name

    # 5. Remove old chunks belonging to this document
    vector_store.delete(
        where={"source": source}
    )

    # 6. Add the new chunks
    vector_store.add_texts(
        texts=chunks,
        metadatas=[
            {"source": source, "chunk": i}
            for i in range(len(chunks))
        ],
        ids=[
            f"{source}_chunk_{i}"
            for i in range(len(chunks))
        ],
    )

    return len(chunks)
