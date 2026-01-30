import numpy as np
import os
import sys
from utils.storage_handler import save_vectors, load_vectors

def verify_salting_integrity():
    # Generate a standard 512-d normalized vector for testing
    test_vector = np.random.rand(512).tolist()
    
    try:
        save_vectors([test_vector])
        retrieved_vectors = load_vectors()
        
        if not retrieved_vectors:
            print("Integrity Error: No vectors retrieved from storage.")
            sys.exit(1)

        if np.allclose(test_vector, retrieved_vectors[0], atol=1e-5):
            print("Salting Integrity: Verified. Obfuscation layer is consistent.")
        else:
            print("Salting Integrity: Failure. Data corruption or salt mismatch.")
            sys.exit(1)
            
    except Exception as e:
        print(f"Privacy test execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify_salting_integrity()