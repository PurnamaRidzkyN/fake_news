def search_similar(collection, query_embedding, top_k=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    ids = results["ids"][0]
    distances = results["distances"][0]

    output = []
    for i in range(len(ids)):
        output.append({
            "id": ids[i],
            "score": distances[i]  # makin kecil = makin mirip
        })

    return output


def search_from_text(collection, model, query_text, top_k=5):
    query_embedding = model.encode(query_text).tolist()
    return search_similar(collection, query_embedding, top_k)