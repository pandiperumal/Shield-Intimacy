import cv2
import sys
from core.pipeline import identity_shield
from modules.identity.registry import registry

def onboard(image_path):
    print(f"--- Onboarding Identity: {image_path} ---")
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read image.")
        return

    # Extract the vector
    result = identity_shield.extract_vectors(img)
    
    if result['identity_present']:
        # Register the first face found
        vector = result['vectors'][0]
        registry.register_user(vector)
        print("✅ Identity SHIELDED. The system will now block intimate content of this person.")
    else:
        print("❌ No face detected. Onboarding failed.")

if __name__ == "__main__":
    # Usage: python app/register.py data/samples/my_face.jpg
    if len(sys.argv) > 1:
        onboard(sys.argv[1])
    else:
        print("Please provide a path to your face image.")