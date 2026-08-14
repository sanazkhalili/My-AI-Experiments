A Retrieval-Augmented Generation (RAG) system that classifies incoming user queries and routes them to the appropriate knowledge base, then retrieves semantically relevant context using ChromaDB and BAAI/bge-m3 embeddings before generating a grounded response via an LLM (through OpenRouter).

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-green)