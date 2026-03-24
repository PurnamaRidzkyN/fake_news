from sentence_transformers import SentenceTransformer
import os

MODEL_DIR = "./models/sentence-transformer"

def get_model():
    if not os.path.exists(MODEL_DIR):
        raise Exception(
            "Model belum ada di local. Jalankan setup.py --step model "
        )

    model = SentenceTransformer(MODEL_DIR)
    return model