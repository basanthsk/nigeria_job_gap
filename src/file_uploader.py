from PyPDF2 import PdfReader
from docx import Document
import io
import streamlit as st

def pdf2text(pdfFileObject):
    reader = PdfReader(pdfFileObject)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def doc2text(docFileObject):
    doc = Document(docFileObject)
    docText = '\n\n'.join(
        paragraph.text for paragraph in doc.paragraphs
    )
    return docText

def get_file_type(uploaded_file):
    file_type = uploaded_file.type
    if file_type is None:
        return "Unknown"
    file_type = file_type.split("/")[1]
    return file_type

def extract_text_from_file(uploaded_file):
    rerun_state = False
    file_type = get_file_type(uploaded_file)
    # st.write("File type: ", file_type)
    
    if file_type == 'pdf':
        return pdf2text(io.BytesIO(uploaded_file.read())), True
        
    elif file_type == 'vnd.openxmlformats-officedocument.wordprocessingml.document':
        return doc2text(io.BytesIO(uploaded_file.read())),True
    else:
        st.info("Only PDF and DOCX files are supported.", icon="ℹ️")
        return "",False

def main():
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'doc'])
    if uploaded_file is not None:
        text = extract_text_from_file(uploaded_file)
        st.text_area('', value=text, height=200)

if __name__ == "__main__":
    main()