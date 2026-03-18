# search_chroma.py

from chroma_db import get_chroma_client

def query_docs(question, top_k=3):
    client = get_chroma_client()
    collection = client.get_collection("docs")
    results = collection.query(query_texts=[question], n_results=top_k)
    return results["documents"]

