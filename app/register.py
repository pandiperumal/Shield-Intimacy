import sys
import argparse
import os
import cv2
from modules.identity.detector import identity_shield
from modules.identity.registry import registry

def main():
    parser = argparse.ArgumentParser(description="Shield-Intimacy: Biometric Registration")
    parser.add_argument("image_path", help="Path to the image for biometric shielding")
    args = parser.parse_args()

    # Load image
    frame = cv2.imread(args.image_path)
    if frame is None:
        print(f"Error: Unable to load image at {args.image_path}")
        sys.exit(1)

    # Extract filename for identity naming (e.g., 'pandi.jpg' -> 'pandi')
    identity_name = os.path.splitext(os.path.basename(args.image_path))[0]

    print(f"Processing registration: {args.image_path} as '{identity_name}'")
    data = identity_shield.extract_vectors(frame)
    
    if data['face_count'] > 0:
        vector = data['vectors'][0]
        
        # Pass the identity name to the registry module
        registry.register_user(vector, identity_name=identity_name)
        
        print(f"Registration successful: Identity '{identity_name}' is shielded.")
    else:
        print("Registration failed: No face detected.")
        sys.exit(1)

if __name__ == "__main__":
    main()