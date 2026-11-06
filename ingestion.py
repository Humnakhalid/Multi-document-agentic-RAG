
from pathlib import Path

import pandas as pd
from docx import Document
from pypdf import PdfReader


def load_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    pages = []

    for page in reader.pages:
        text = page.extract_text(extraction_mode="layout")
        if text:
            pages.append(text)

    return "\n".join(pages)


def load_docx(file_path: str) -> str:
    document = Document(file_path)
    return "\n".join(
        paragraph.text for paragraph in document.paragraphs
    )


def load_txt(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def load_csv(file_path: str) -> str:
    dataframe = pd.read_csv(file_path)
    return dataframe.to_string(index=False)


def load_document(file_path: str) -> str:
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return load_pdf(file_path)
    elif extension == ".docx":
        return load_docx(file_path)
    elif extension == ".txt":
        return load_txt(file_path)
    elif extension == ".csv":
        return load_csv(file_path)
    else:
        raise ValueError(f"Unsupported file type: {extension}")
