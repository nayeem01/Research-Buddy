import io
from PyPDF2 import PdfReader

from langchain_text_splitters import CharacterTextSplitter


def get_pdf_text(pdfs):
    text = ""

    for pdf in pdfs:
        file_binary = pdf.file.read()
        pdf_file = io.BytesIO(file_binary)
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text().replace("\n", " ")

    return text


def get_text_chunks(text):
    print("text", text)
    text_splitter = CharacterTextSplitter(
        chunk_size=500, chunk_overlap=50, separator=""
    )
    chunks = text_splitter.split_text(text)
    return chunks
