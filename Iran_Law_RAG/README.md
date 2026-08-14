A Retrieval-Augmented Generation (RAG) system that classifies incoming user queries and routes them to the appropriate knowledge base, then retrieves semantically relevant context using ChromaDB and BAAI/bge-m3 embeddings before generating a grounded response via an LLM (through OpenRouter).

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-green)

## 📁 Project structure

```
.
├── src/
│   ├── config.py           # settings and prompts
│   ├── utils.py             # connect to collections
│   └── chat_engine.py       # routing and using LLM
├── database/
│   ├── crud.py           # create, read in database
│   ├── embedding_functions.py             # save embeddings and retrieval
│   └── save_info.py      # save information about rules in database
├── app.py                   # Gradio app
├── requirements.txt
├── .env.example
└── README.md
```