import logging
from nudenet import NudeDetector

logger = logging.getLogger(__name__)

class NSFWDetector:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NSFWDetector, cls).__new__(cls)
            logger.info("Loading NudeNet Detector weights...")
            # This triggers the 100MB download on the first run only
            cls._instance.detector = NudeDetector()
        return cls._instance

    def get_score(self, image_path: str) -> float:
        """
        Returns the probability (0.0 to 1.0) of sexual content.
        """
        try:
            results = self.detector.detect(image_path)
            # NudeNet returns a list of detections. 
            # We look for the highest confidence in 'exposed' categories.
            high_risk_classes = [
                "BUTTOCKS_EXPOSED", "FEMALE_BREAST_EXPOSED", 
                "FEMALE_GENITALIA_EXPOSED", "MALE_GENITALIA_EXPOSED"
            ]
            
            max_score = 0.0
            for detection in results:
                if detection['class'] in high_risk_classes:
                    if detection['score'] > max_score:
                        max_score = detection['score']
            
            return max_score
        except Exception as e:
            logger.error(f"NSFW Triage failed: {e}")
            return 0.0

# Export the instance
nsfw_gate = NSFWDetector()