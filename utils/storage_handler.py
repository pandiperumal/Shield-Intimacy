import numpy as np
import os
import logging

logger = logging.getLogger(__name__)

DB_PATH = "data/registry.npz"

def save_vectors(vectors_list):
    """Saves the list of 512-d embeddings to disk."""
    try:
        # Convert list to a numpy array for efficient storage
        arr = np.array(vectors_list, dtype=np.float32)
        np.savez_compressed(DB_PATH, embeddings=arr)
        logger.info(f"✅ Registry saved to {DB_PATH}")
    except Exception as e:
        logger.error(f"Failed to save registry: {e}")

def load_vectors():
    """Loads embeddings from disk."""
    if not os.path.exists(DB_PATH):
        return []
    try:
        data = np.load(DB_PATH)
        return data['embeddings'].tolist()
    except Exception as e:
        logger.error(f"Failed to load registry: {e}")
        return []