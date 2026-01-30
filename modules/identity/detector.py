import logging
import cv2
import numpy as np
from insightface.app import FaceAnalysis

logger = logging.getLogger(__name__)

class IdentityShield:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IdentityShield, cls).__new__(cls)
            cls._instance.app = FaceAnalysis(
                name='buffalo_l', 
                providers=['CPUExecutionProvider']
            )
            cls._instance.app.prepare(ctx_id=0, det_size=(640, 640))
        return cls._instance

    def extract_vectors(self, image_array: np.ndarray):
        try:
            faces = self.app.get(image_array)
            embeddings = []
            
            for face in faces:
                if face.det_score > 0.4: 
                    embeddings.append(face.normed_embedding.tolist())
            
            return {
                "identity_present": len(embeddings) > 0,
                "face_count": len(embeddings),
                "confidence": [float(f.det_score) for f in faces],
                "vectors": embeddings
            }
        except Exception as e:
            logger.error(f"Identity extraction failed: {e}")
            return {
                "identity_present": False, 
                "face_count": 0, 
                "vectors": []
            }

identity_shield = IdentityShield()