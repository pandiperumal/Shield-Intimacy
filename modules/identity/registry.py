import numpy as np
from utils.storage_handler import save_vectors, load_vectors
from scipy.spatial.distance import cosine

class ConsentRegistry:
    def __init__(self):
        # Load existing shielded users from disk on startup
        self.shielded_vectors = load_vectors()

    def register_user(self, embedding):
        """Adds a user and immediately persists to disk."""
        self.shielded_vectors.append(embedding)
        save_vectors(self.shielded_vectors)

    def check_consent(self, detected_embedding, threshold=0.65):
        """Standard Cosine Similarity match."""
        if not self.shielded_vectors:
            return False
            
        for shielded_vec in self.shielded_vectors:
            dist = cosine(detected_embedding, shielded_vec)
            if (1 - dist) > threshold:
                return True
        return False

registry = ConsentRegistry()