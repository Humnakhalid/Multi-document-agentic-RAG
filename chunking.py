
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )

    chunks = splitter.split_text(text)
    return chunks
