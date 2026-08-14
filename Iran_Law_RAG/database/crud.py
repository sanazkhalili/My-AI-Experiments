import chromadb

def create_db(path='./database/test'):
    client = chromadb.PersistentClient(path)
    return client


def create_collection(client, name):
    collection = client.get_or_create_collection(name=name,
                                    metadata={"hnsw:space": "cosine"})
    return collection


def add2collection(collection, ids, documents, embeddings, metadatas):
    collection.add(ids=ids,
               documents=documents, 
               embeddings=embeddings, 
               metadatas=metadatas)


def get_by_id(collection, ids, include=None):
    if include:
        return collection.get(ids=ids, include=include)
    return collection.get(ids=ids)


def filter_metadata(collection, cond):
    result = collection.get(where=cond)
    return result



def get_similar2query(collection, embedding_query, num_res):
    results = collection.query(query_embeddings=embedding_query,
                               n_results=num_res)
    result = ''

    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        if meta and meta.get("chapter"):

            print(f"فاصله: {dist:.4f} | فصل: {meta.get('chapter')}")
            print(doc)
            result += (
                f"فاصله: {dist:.4f}\n"
                f"فصل: {meta['chapter']}\n\n"
                f"{doc}\n"
                "------------------------\n"
            )
        else:
            result+=(f"{doc}\n"
                "------------------------\n")
    return result

