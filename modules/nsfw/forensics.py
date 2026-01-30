import cv2
import numpy as np
import os

class ForensicAnalyzer:
    def __init__(self):
        self.temp_path = "data/temp_ela.jpg"
        self.quality = 90

    def detect_synthetic_artifacts(self, image_path):
        original = cv2.imread(image_path)
        if original is None: 
            return 0.1

        cv2.imwrite(self.temp_path, original, [cv2.IMWRITE_JPEG_QUALITY, self.quality])
        
        temporary = cv2.imread(self.temp_path)
        diff = cv2.absdiff(original, temporary)
        
        d_mean = np.mean(diff)
        if d_mean == 0: 
            return 1.0
            
        scale = 255.0 / d_mean
        diff = cv2.convertScaleAbs(diff, alpha=scale)
        
        gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        entropy = np.var(gray_diff)
        
        if os.path.exists(self.temp_path):
            os.remove(self.temp_path)

        if entropy < 20000:
            score = 0.8
        else:
            score = 0.1
            
        return float(np.clip(score, 0.0, 1.0))

forensic_engine = ForensicAnalyzer()