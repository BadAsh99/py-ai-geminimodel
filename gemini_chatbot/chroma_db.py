# chroma_db.py

import chromadb
from chromadb.config import Settings

def get_chroma_client():
    return chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chroma_db"
    ))

