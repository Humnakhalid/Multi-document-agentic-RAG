import uuid
from pathlib import Path

import streamlit as st

from document_processor import process_document
from rag_pipeline import ask_question


# 1. Configure the page
st.set_page_config(
    page_title="Local RAG Chatbot",
    page_icon="📚",
    layout="centered",
)

st.title("📚 Local RAG Chatbot")
st.caption("Upload your documents and ask questions about their content.")

# 2. Create a folder for uploaded documents
UPLOAD_DIR = Path("uploaded_documents")
UPLOAD_DIR.mkdir(exist_ok=True)

# 3. Upload documents
st.subheader("📁 Upload your documents")

uploaded_files = st.file_uploader(
    "Choose your documents",
    type=["pdf", "docx", "txt", "csv"],
    accept_multiple_files=True,
)

# 4. Process uploaded documents when the button is clicked
if st.button("Process documents", type="primary"):
    if not uploaded_files:
        st.warning("Please upload at least one document.")
    else:
        for uploaded_file in uploaded_files:
            try:
                original_name = Path(uploaded_file.name).name
                unique_name = f"{uuid.uuid4().hex}_{original_name}"
                file_path = UPLOAD_DIR / unique_name

                file_path.write_bytes(uploaded_file.getvalue())

                with st.spinner(f"Processing {uploaded_file.name}..."):
                    chunk_count = process_document(str(file_path))

                st.success(
                    f"{uploaded_file.name}: indexed {chunk_count} chunks."
                )

            except Exception as error:
                st.error(
                    f"Could not process {uploaded_file.name}: {error}"
                )

st.divider()

# 5. Initialize conversation history 
if "messages" not in st.session_state:
    st.session_state.messages = []

# 6. Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. Accept a new question
question = st.chat_input("Ask a question about your documents...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # 8. Call the RAG pipeline
    with st.chat_message("assistant"):
        with st.spinner("Searching documents and generating an answer..."):
            try:
                answer = ask_question(question)
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as error:
                st.error(f"Something went wrong: {error}")
