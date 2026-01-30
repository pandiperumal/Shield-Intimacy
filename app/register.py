import sys
import argparse
import cv2
from modules.identity.detector import identity_shield
from modules.identity.registry import registry

def main():
    parser = argparse.ArgumentParser(description="Shield-Intimacy: Biometric Registration")
    parser.add_argument("image_path", help="Path to the image for biometric shielding")
    args = parser.parse_args()

    frame = cv2.imread(args.image_path)
    if frame is None:
        print(f"Error: Unable to load image at {args.image_path}")
        sys.exit(1)

    print(f"Processing registration: {args.image_path}")
    data = identity_shield.extract_vectors(frame)
    
    if data['face_count'] > 0:
        vector = data['vectors'][0]
        registry.register_user(vector)
        print(f"Registration successful: Identity from {args.image_path} is shielded.")
    else:
        print("Registration failed: No face detected in the provided image.")
        sys.exit(1)

if __name__ == "__main__":
    main()