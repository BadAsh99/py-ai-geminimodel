# store_pdf_in_chroma.py

from chroma_db import get_chroma_client
import fitz  # PyMuPDF
import uuid

def store_pdf(path, source_name="uploaded_pdf"):
    client = get_chroma_client()
    collection = client.get_or_create_collection(name="docs")

    doc = fitz.open(path)
    for i, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            collection.add(
                documents=[text],
                metadatas=[{"page": i + 1, "source": source_name}],
                ids=[str(uuid.uuid4())]
            )

