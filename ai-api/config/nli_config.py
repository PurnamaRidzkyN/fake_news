from sentence_transformers import CrossEncoder
import os

MODEL_DIR = "./models/nli"

def get_nli_model():
    if not os.path.exists(MODEL_DIR):
        raise Exception("Model NLI belum ada. Jalankan setup untuk download.")

    model = CrossEncoder(MODEL_DIR)
    return model