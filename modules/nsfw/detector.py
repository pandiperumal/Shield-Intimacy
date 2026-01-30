import logging
from nudenet import NudeDetector

logger = logging.getLogger(__name__)

class NSFWDetector:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NSFWDetector, cls).__new__(cls)
            cls._instance.detector = NudeDetector()
        return cls._instance

    def get_score(self, image_path: str) -> float:
        try:
            results = self.detector.detect(image_path)
            high_risk_classes = {
                "BUTTOCKS_EXPOSED", "FEMALE_BREAST_EXPOSED", 
                "FEMALE_GENITALIA_EXPOSED", "MALE_GENITALIA_EXPOSED"
            }
            
            max_score = 0.0
            for detection in results:
                if detection['class'] in high_risk_classes:
                    if detection['score'] > max_score:
                        max_score = detection['score']
            
            return float(max_score)
        except Exception as e:
            logger.error(f"NSFW detection failure: {e}")
            return 0.0

nsfw_gate = NSFWDetector()