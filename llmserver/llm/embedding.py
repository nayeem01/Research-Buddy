import os
import io
from PyPDF2 import PdfReader

from langchain_community.document_loaders import PyPDFDirectoryLoader

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
)

from langchain_voyageai import VoyageAIEmbeddings

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore


def get_pdf_text(pdfs):
    # file_loader = PyPDFDirectoryLoader("papers/")
    # documents = file_loader.load()
    # loader = PyPDFLoader("example_data/layout-parser-paper.pdf")
    text = ""

    for pdf in pdfs:
        file_binary = pdf.file.read()
        pdf_file = io.BytesIO(file_binary)
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text().replace("\n", " ")

    return text


def get_text_chunks(text):
    # text_splitter = CharacterTextSplitter(
    #     chunk_size=500, chunk_overlap=50, separator=""
    # )
    # chunks = text_splitter.split_text(text)
    text_splitter = CharacterTextSplitter(
        separator="", chunk_size=250, chunk_overlap=50
    )
    doc = text_splitter.split_text(text)
    # print(len(doc))
    return doc


def create_embedding(text_chunks):
    embeddings = VoyageAIEmbeddings(
        voyage_api_key=os.environ.get("VOYAGE_API_KEY"), model="voyage-law-2"
    )
    docs = embeddings.embed_documents(text_chunks)
    return docs


def vector_store(embeddings, index_name, namespace):
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

    indexes = pc.list_indexes()
    index_names = [index.name for index in indexes]
    # embedding_data = embeddings.embeddings

    if index_name not in index_names:
        print(f"Index '{index_name}' does not exist.")

        embedding_dimension = len(embeddings[0])

        pc.create_index(
            index_name,
            embedding_dimension,
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

        index = pc.Index(index_name)

        data = [{"id": str(i), "values": emb} for i, emb in enumerate(embeddings)]

        index.upsert(data, namespace=namespace)

        print(f"\nInserted {len(embeddings)} documents into Pinecone.")

        return {"status": "success"}

    return {"status": "index already exists"}
    # return {docsearch}


def search_query(query, index_name, namespace):
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
    index = pc.Index(index_name)
    search_results = index.query(
        queries=[{"query": query}], namespace=namespace, top_k=10
    )
    print(search_results)
    return search_results
