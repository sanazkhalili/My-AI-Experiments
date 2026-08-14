import crud
import embedding_functions

fp = open('rule_info.txt', encoding='utf-8')
text = fp.readlines()

client = crud.create_db()
collection = crud.create_collection(client=client, name='rules')
create_embeddings.save_embedding_info_mainrule(text , create_embeddings.model, collection)
