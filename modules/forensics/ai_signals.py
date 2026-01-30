import cv2
import numpy as np

def detect_ai_artifacts(image_array):
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    
    dft = np.fft.fft2(gray)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(np.abs(dft_shift) + 1)
    
    mean_val = np.mean(magnitude_spectrum)
    is_synthetic = mean_val > 100 
    
    return {
        "ai_generated_probability": 0.85 if is_synthetic else 0.15,
        "frequency_mean": float(mean_val)
    }