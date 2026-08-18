A Retrieval-Augmented Generation (RAG) system that classifies incoming user queries and routes them to the appropriate knowledge base, then retrieves semantically relevant context using ChromaDB and BAAI/bge-m3 embeddings before generating a grounded response via an LLM (through OpenRouter).

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-green)


<p align="center">
  <img src="E:\Our_company\GitHub_ai_expriment\Iran_Law_RAG\assert\demo.gif" width="700">
</p>

## 📁 Project structure

```
.
├── src/
│   ├── config.py            # settings and prompts
│   ├── utils.py             # connect to collections
│   └── chat_engine.py       # routing and using LLM
├── database/
│   ├── crud.py                            # create, read in database
│   ├── embedding_functions.py             # save embeddings and retrieval
│   └── save_embeddings.py                 # indexing(save information about rules in database)
├── app.py                                 # Gradio app
├── env
└── README.md
```
Run step by step
````
python ./database/save_embeddings.py

python ./src/main.py

````
## APP Components

| Component | Model / Tool |
|-----------|--------------|
| UI | Gradio |
| Embedding Model | BAAI/bge-m3 |
| LLM | cohere/north-mini-code:free (OpenRouter) |
| Vector Database | ChromaDB |


## Limitations of the First Version

- **Low response speed:** One of the main reasons was the redundant use of the LLM twice in the pipeline.
- **Code quality improvements:** The code structure requires further cleaning, refactoring, and better organization.
- **Lack of evaluation module:** The first version does not include an evaluation pipeline for measuring retrieval and answer accuracy.