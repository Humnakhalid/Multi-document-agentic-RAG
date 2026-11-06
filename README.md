
# Multi-Document Agentic RAG

A Multi-Document Retrieval-Augmented Generation (RAG) application built with Python and local LLMs using Ollama.

## Features

- Upload and process multiple documents.
- Support document-based question answering.
- Intelligent document chunking.
- Generate vector embeddings.
- Store embeddings using ChromaDB.
- Retrieve relevant document chunks.
- Generate context-aware answers using a local LLM.

## Technologies Used

- Python
- Streamlit
- LangChain
- LangGraph
- ChromaDB
- Ollama
- Qwen 2.5 (1.5B)
- Nomic Embed Text

## Project Structure

```text
RAG/
├── app.py
├── chunking.py
├── document_processor.py
├── embeddings.py
├── generator.py
├── ingestion.py
├── rag_pipeline.py
├── retriever.py
├── vector_store.py
├── sample_documents/
├── uploaded_documents/
├── chroma_db/
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd Multi-document-agentic-RAG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and the required models are available:

```bash
ollama pull qwen2.5:1.5b
ollama pull nomic-embed-text
```

## Run the Application

```bash
streamlit run app.py
```

## Future Improvements

- Advanced retrieval strategies.
- Hybrid search.
- Reranking.
- Hallucination reduction.
- Improved agentic reasoning.

## Author

Developed as a hands-on project to explore Agentic RAG and local LLM applications.
