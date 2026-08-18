import crud
from embedding_functions import save_embedding_info_mainrule, save_embed
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")

fp = open(r'D:\...\My-AI-Experiments\Iran_Law_RAG\data\info_rules.txt', encoding='utf-8')
text = fp.readlines()

client = crud.create_db()

# create a collection for rules info
collection = crud.create_collection(client=client, name='rules_info')
save_embedding_info_mainrule(text , model, collection)

# create a collection for main rules
collection = crud.create_collection(client=client, name='rules')
save_embed(collection, model)

