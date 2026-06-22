# AI Document Intelligence System (RAG + Semantic Search)

A production-style AI system for uploading documents, extracting text, and performing semantic search and question answering using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Multi-format document support (PDF, DOCX, TXT, Images)
- 🔍 Text extraction (OCR + parser-based)
- 🧠 Semantic search using FAISS + Sentence Transformers
- 💬 Question answering over documents (RAG-based)
- 🧩 Chunking + embedding pipeline
- 🧠 AI fallback summarization (works without API key)
- ⚡ FastAPI backend (production-ready structure)

---
It supports:

📄 Multi-format document ingestion (PDF, DOCX, TXT, images via OCR)
🧠 RAG-based semantic search using vector embeddings
💬 Chat-with-document interface (Ask questions directly on uploaded files)
🔍 Intelligent text chunking and retrieval system
📊 Automatic document insights (keywords, summaries, complexity analysis)
⚡ Hybrid AI pipeline (OpenAI + fallback local logic)
🧱 Modular architecture designed for scalability and production deployment

The system is designed as a foundation for enterprise-level document AI systems, combining information retrieval and generative AI.
----

## 🏗️ Architecture

Upload File
↓
Text Extraction
↓
Chunking
↓
Embedding (SentenceTransformer)
↓
Vector Store (FAISS)
↓
Semantic Search
↓
Answer Generation (RAG)

