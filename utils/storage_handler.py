import logging
import os
import numpy as np

logger = logging.getLogger(__name__)

DB_PATH = "data/registry.npz"
SYSTEM_SALT = np.array([0.123, 0.456] * 256, dtype=np.float32)

def save_vectors(vectors_list):
    try:
        salted = [np.array(v, dtype=np.float32) + SYSTEM_SALT for v in vectors_list]
        arr = np.array(salted, dtype=np.float32)
        
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        np.savez_compressed(DB_PATH, embeddings=arr)
    except Exception as e:
        logger.error(f"Registry persistence failure: {e}")

def load_vectors():
    if not os.path.exists(DB_PATH):
        return []
    try:
        data = np.load(DB_PATH)
        embeddings = data['embeddings']
        return [v - SYSTEM_SALT for v in embeddings]
    except Exception as e:
        logger.error(f"Registry retrieval failure: {e}")
        return []