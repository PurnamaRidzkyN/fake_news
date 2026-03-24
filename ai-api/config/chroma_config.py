import chromadb

CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "lensa_hoaks"

def get_chroma_collection():
    client = chromadb.PersistentClient(path=CHROMA_DIR)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection