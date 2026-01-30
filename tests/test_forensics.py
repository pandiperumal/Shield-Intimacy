import os
import sys
from modules.nsfw.forensics import forensic_engine

def run_forensic_audit(directory_path="data/samples"):
    if not os.path.exists(directory_path):
        print(f"Error: Directory not found at {directory_path}")
        sys.exit(1)

    # Dynamically grab all image files from the directory
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    targets = [f for f in os.listdir(directory_path) if f.lower().endswith(valid_extensions)]

    if not targets:
        print(f"No valid images found in {directory_path}")
        return

    print(f"{'FILE':<30} | {'SCORE'}")
    print("-" * 45)

    for target in sorted(targets):
        path = os.path.join(directory_path, target)
        score = forensic_engine.detect_synthetic_artifacts(path)
        print(f"{target:<30} | {score:.4f}")

if __name__ == "__main__":
    run_forensic_audit()