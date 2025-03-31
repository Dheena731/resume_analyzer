import os
import tempfile
from langchain_community.document_loaders import PDFPlumberLoader
from docx import Document

# Function to handle file upload and text extraction
def extract_text_from_resume(uploaded_file):
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.type.split('/')[-1]}") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    raw_resume_text = ""

    # Handle PDF files
    if uploaded_file.type == "application/pdf":
        loader = PDFPlumberLoader(temp_file_path)
        documents = loader.load_and_split()
        raw_resume_text = "\n".join([doc.page_content for doc in documents])

    # Handle DOCX files
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(temp_file_path)
        raw_resume_text = "\n".join([paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()])

    # Remove temporary file after processing
    os.remove(temp_file_path)

    return raw_resume_text
