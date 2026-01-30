import os
import sys
import argparse
from core.pipeline import ShieldPipeline

def run_system_test(test_dir):
    if not os.path.exists(test_dir):
        print(f"Error: Directory not found at {test_dir}")
        sys.exit(1)

    engine = ShieldPipeline()
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
    
    files = [f for f in os.listdir(test_dir) if f.lower().endswith(valid_extensions)]
    
    if not files:
        print(f"No valid images found in {test_dir}")
        return

    print(f"{'IMAGE':<30} | {'VERDICT':<30} | {'AI SCORE':<8} | {'SHIELDED'}")
    print("-" * 85)

    for filename in sorted(files):
        image_path = os.path.join(test_dir, filename)
        result = engine.process_image(image_path)
        
        print(f"{filename:<30} | "
              f"{result['verdict']:<30} | "
              f"{result['forensic_score']:<8.4f} | "
              f"{result['identity_shielded']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shield-Intimacy: System Integration Test")
    parser.add_argument("--dir", default="data/samples", help="Directory containing test images")
    args = parser.parse_args()
    
    run_system_test(args.dir)