from core.pipeline import ShieldPipeline
import os

def main():
    pipeline = ShieldPipeline()
    sample = "data/samples/pandi2.jpg"
    
    if os.path.exists(sample):
        print(f"--- Starting Analysis on {sample} ---")
        result = pipeline.process_image(sample)
        print(result)
    else:
        print("Error: data/samples/test.jpg not found.")

if __name__ == "__main__":
    main()