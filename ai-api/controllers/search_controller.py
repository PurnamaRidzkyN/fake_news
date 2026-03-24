from flask import request, jsonify
from services.chroma_service import search_from_text

def search_controller(collection, model):
    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Query tidak ditemukan"}), 400

    query = data["query"]
    top_k = data.get("top_k", 5)

    try:
        results = search_from_text(collection, model, query, top_k)

        return jsonify({
            "query": query,
            "top_k": top_k,
            "results": results
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500