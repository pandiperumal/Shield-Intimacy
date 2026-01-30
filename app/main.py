import argparse
from core.pipeline import ShieldPipeline

def main():
    parser = argparse.ArgumentParser(description="Shield-Intimacy: Inference Engine")
    parser.add_argument("image_path", help="Path to the image to analyze")
    
    args = parser.parse_args()
    engine = ShieldPipeline()
    
    result = engine.process_image(args.image_path)
    
    print("\n--- INFERENCE RESULT ---")
    for key, value in result.items():
        print(f"{key.upper()}: {value}")

if __name__ == "__main__":
    main()