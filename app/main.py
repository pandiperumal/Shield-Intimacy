import argparse
from core.pipeline import ShieldPipeline

def main():
    parser = argparse.ArgumentParser(description="Shield-Intimacy: Inference Engine")
    parser.add_argument("image_path", help="Path to the image to analyze")
    args = parser.parse_args()
    
    engine = ShieldPipeline()
    result = engine.process_image(args.image_path)
    
    # This block is critical for terminal output
    print("\n" + "="*40)
    print("      SHIELD-INTIMACY VERDICT")
    print("="*40)
    for key, value in result.items():
        print(f"{key.upper():<20}: {value}")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()