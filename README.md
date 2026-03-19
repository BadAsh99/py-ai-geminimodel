# PY-AI-GeminiModel

> Context-aware document Q&A chatbot powered by Google Gemini and ChromaDB RAG

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.33-red?logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-green)

---

## Overview

A Python-based AI chatbot that combines **Google Gemini** with **Retrieval-Augmented Generation (RAG)** using ChromaDB as the vector store. Users upload PDF and CSV documents, which are chunked, embedded, and stored in a local Chroma collection. Questions are answered by retrieving semantically relevant chunks and passing them as context to Gemini — giving accurate, document-grounded responses instead of hallucinated answers.

---

## Architecture

```
Document Ingestion
    │
    ├── PDF (PyMUPDF)   →  Text extraction  →  Chunks
    └── CSV (Pandas)    →  Row conversion   →  Chunks
            │
            ▼
    store_pdf_in_chroma.py
        └── Gemini Embeddings → ChromaDB vector store
                │
                ▼
    Q&A Flow
        │
        ├── User question
        │       └── search_chroma.py
        │               └── Similarity search → Top-K relevant chunks
        │
        └── gemini_chat.py
                └── prompt = retrieved_chunks + user_question
                        └── Gemini API → Streaming response
                                └── Streamlit write_stream() → UI
```

---

## Features

- **RAG pipeline** — retrieves semantically relevant document chunks before generating answers, reducing hallucination
- **PDF processing** — full text extraction from multi-page PDFs using PyMUPDF
- **CSV ingestion** — tabular data converted to natural language context
- **ChromaDB vector store** — local persistent embedding store, no external vector DB required
- **Streaming responses** — real-time answer generation via Gemini's streaming API
- **Streamlit UI** — clean web interface with file upload, model selection, and chat history
- **Session logging** — all Q&A exported to CSV for audit or knowledge base use
- **Multi-model** — toggle between Gemini models and GPT-4

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| AI | Google Gemini API (gemini-1.5-flash, gemini-2.5-pro) |
| Vector Store | ChromaDB (local persistent) |
| Embeddings | Gemini Embeddings API |
| PDF Processing | PyMUPDF (fitz) |
| Data | Pandas 2.2 |
| UI | Streamlit 1.33 |
| Fallback LLM | OpenAI GPT-4 |
| Config | python-dotenv |

---

## Getting Started

```bash
git clone https://github.com/BadAsh99/py-ai-geminimodel.git
cd py-ai-geminimodel/gemini_chatbot
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add GOOGLE_API_KEY
```

### Ingest Documents

```bash
# Store PDF in ChromaDB
python store_pdf_in_chroma.py --file data/your-document.pdf

# Verify embeddings
python search_chroma.py --query "test query"
```

### Run the App

```bash
streamlit run streamlit_app.py
```

---

## Environment Variables

```env
GOOGLE_API_KEY=
OPENAI_API_KEY=    # optional, for GPT-4 fallback
```

---

## File Structure

```
gemini_chatbot/
├── streamlit_app.py        # Main Streamlit UI
├── gemini_chat.py          # Gemini API integration + streaming
├── store_pdf_in_chroma.py  # PDF ingestion → ChromaDB
├── search_chroma.py        # Semantic search against vector store
├── chroma_db.py            # ChromaDB client configuration
├── chat_logger.py          # Session log to CSV
├── main.py                 # CLI entry point
├── utils/
│   └── loader.py           # PDF + CSV loaders
└── data/                   # Document storage
```

---

## Use Cases

- Ask questions about large PDF documentation without reading it all
- Query tabular data in natural language
- Build a knowledge base Q&A tool for any document set
- Prototype RAG architecture for production AI applications

---

## Author

**Ash Clements** — Sr. Principal Security Consultant | AI & Cloud Security
[github.com/BadAsh99](https://github.com/BadAsh99)
