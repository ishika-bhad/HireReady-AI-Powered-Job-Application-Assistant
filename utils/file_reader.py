import PyPDF2
import docx
import streamlit as st

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

def load_resume(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        return read_pdf(uploaded_file)
    elif uploaded_file.name.endswith('.docx'):
        return read_docx(uploaded_file)
    else:
        st.error("Unsupported file format")
        return None
