from sentence_transformers import SentenceTransformer
import json 
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from database.crud import add2collection, create_db, create_collection
from database import crud

model = SentenceTransformer("BAAI/bge-m3")

def save_json(file_name, data):
     with open(file_name, "w", encoding="utf-8") as f:
          json.dump(data, f, ensure_ascii=False, indent=2)

def read_json_data():
    with open("main_rule.json", encoding='utf-8') as f:
         articles =json.load(f)
    return articles


def save_embed(collection, embed_model):
    with open("main_rule.json", encoding='utf-8') as f:
         articles =json.load(f)

    articles= articles
    texts_to_embed = [f"{a['chapter']}. {a['asl']}: {' '.join(a['text'])}" for a in articles]

    embeddings = embed_model.encode(texts_to_embed, normalize_embeddings=True) 

    add2collection(collection=collection,
        ids=[f"article_{i}" for i in range(len(articles))],
        embeddings=embeddings.tolist(),          
        documents=[" ".join(a["text"]) for a in articles],   
        metadatas=[{"chapter": a["chapter"], "article_label": a["asl"]} for a in articles]
    )

def remove_prep_database(rm_name):
     client = create_db()
     #client.delete_collection(rm_name)
     collection = create_collection(client, name=rm_name)
     return collection

def get_similar_answer(collection, message):
     embed_query = model.encode(f"query:{message}")
     d = crud.get_similar2query(collection=collection,
                                embedding_query=[embed_query],
                                num_res=2)
     return d

def get_similar_info(collection, message):
     embed_query = model.encode(f"query:{message}")
     d = crud.get_similar2query(collection=collection,
                                embedding_query=[embed_query],
                                num_res=2)
     return d
     

def save_embedding_info_mainrule(text , embed_model, collection):
     embeddings = embed_model.encode(text, normalize_embeddings=True) 
     collection.add(ids=[f"info_{i}" for i in range(len(text))],
                    documents= text, 
                    embeddings=embeddings.tolist())
     