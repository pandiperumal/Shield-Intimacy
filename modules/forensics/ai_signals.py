import cv2
import numpy as np

def detect_ai_artifacts(image_array):
    """
    Analyzes the frequency domain of the image to find 'synthetic' patterns.
    """
    # 1. Convert to grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    
    # 2. Perform FFT (Fast Fourier Transform)
    dft = np.fft.fft2(gray)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(np.abs(dft_shift) + 1)
    
    # 3. Simple Industry Heuristic: 
    # AI images often have high energy in high-frequency corners.
    mean_val = np.mean(magnitude_spectrum)
    
    # This is a placeholder for a real AI-detector model
    # If the mean frequency energy is weird, we flag it.
    is_synthetic = mean_val > 100 # This threshold requires tuning
    
    return {
        "ai_generated_probability": 0.85 if is_synthetic else 0.15,
        "frequency_mean": float(mean_val)
    }