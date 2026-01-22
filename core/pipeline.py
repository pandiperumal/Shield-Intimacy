import cv2
import logging
from modules.nsfw.detector import nsfw_gate
from modules.identity.detector import identity_shield
from modules.identity.registry import registry
from core.decision_engine import aggregate_signals

logger = logging.getLogger("Pipeline")

class ShieldPipeline:
    def process_image(self, image_path: str):
        """
        Main industrial pipeline: Triage -> Identity -> Consent -> Verdict.
        """
        # 1. Load pixels once (Industrial efficiency)
        frame = cv2.imread(image_path)
        if frame is None:
            return {"status": "error", "message": "Image load failure"}

        # 2. Stage 1: Triage (Is it intimate?)
        nsfw_score = nsfw_gate.get_score(image_path)

        # 3. Stage 2: Identity & Consent (Who is it?)
        # We only run expensive identity checks if NSFW score is > 0.3
        identity_data = {"identity_present": False, "face_count": 0, "vectors": []}
        is_shielded = False
        
        if nsfw_score > 0.3:
            identity_data = identity_shield.extract_vectors(frame)
            
            # Check detected faces against the Shielded Registry
            for vec in identity_data.get('vectors', []):
                if registry.check_consent(vec):
                    is_shielded = True
                    break

        # 4. Stage 3: Final Decision Engine
        verdict = aggregate_signals(
            nsfw_score=nsfw_score,
            identity_found=identity_data['identity_present'],
            is_shielded=is_shielded,
            ai_score=0.15  # Placeholder for forensics module
        )

        # 5. Result Aggregation
        return {
            "verdict": verdict,
            "nsfw_score": round(float(nsfw_score), 4),
            "face_detected": identity_data['identity_present'],
            "face_count": identity_data['face_count'],
            "identity_shielded": is_shielded
        }