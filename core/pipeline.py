import cv2
import logging
from modules.nsfw.detector import nsfw_gate
from modules.identity.detector import identity_shield
from modules.identity.registry import registry
from modules.nsfw.forensics import forensic_engine
from core.decision_engine import aggregate_signals

logger = logging.getLogger("Pipeline")

class ShieldPipeline:
    def process_image(self, image_path: str):
        frame = cv2.imread(image_path)
        if frame is None:
            return {"status": "error", "message": "Image load failure"}

        nsfw_score = nsfw_gate.get_score(image_path)
        forensic_score = forensic_engine.detect_synthetic_artifacts(image_path)

        identity_data = {"identity_present": False, "face_count": 0, "vectors": []}
        is_shielded = False
        
        identity_data = identity_shield.extract_vectors(frame)
        
        for vec in identity_data.get('vectors', []):
            if registry.check_consent(vec):
                is_shielded = True
                break

        verdict = aggregate_signals(
            nsfw_score=nsfw_score,
            identity_found=identity_data['identity_present'],
            is_shielded=is_shielded,
            ai_score=forensic_score  
        )

        return {
            "verdict": verdict,
            "nsfw_score": round(float(nsfw_score), 4),
            "forensic_score": round(float(forensic_score), 4),
            "face_detected": identity_data['identity_present'],
            "face_count": identity_data['face_count'],
            "identity_shielded": is_shielded
        }