import os
import numpy as np

class ConsentRegistry:
    def __init__(self, registry_path="data/registry"):
        self.registry_path = registry_path
        # Ensure directory exists for multi-file storage
        os.makedirs(self.registry_path, exist_ok=True)

    def calculate_similarity(self, feat1, feat2):
        """Standard Cosine Similarity for Buffalo_L embeddings."""
        return np.dot(feat1, feat2) / (np.linalg.norm(feat1) * np.linalg.norm(feat2))

    def register_user(self, vector, identity_name):
        """Saves a salted biometric vector as an individual file named after the image."""
        # Note: Add your salting logic here if required
        save_path = os.path.join(self.registry_path, f"{identity_name}.npz")
        np.savez(save_path, vector=vector)
        print(f"Successfully saved identity to: {save_path}")

    def check_consent(self, extracted_vector):
        """Iterate through all registered .npz files to find a match."""
        if not os.path.exists(self.registry_path):
            return False
            
        for file in os.listdir(self.registry_path):
            if file.endswith(".npz"):
                file_path = os.path.join(self.registry_path, file)
                data = np.load(file_path)
                stored_vector = data['vector']
                
                similarity = self.calculate_similarity(extracted_vector, stored_vector)
                
                # Useful for debugging during your presentation
                # print(f"Checking {file}: Similarity {similarity:.4f}")
                
                if similarity > 0.65:
                    return True  
        return False

# Initialize the instance for app-wide use
registry = ConsentRegistry()