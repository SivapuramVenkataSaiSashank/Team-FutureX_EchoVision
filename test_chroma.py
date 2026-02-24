import sys
import os

# Ensure src in path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from document_processor import DocumentProcessor

def test_chroma():
    dp = DocumentProcessor()
    
    # We need a small test file
    test_file_path = "test_chroma_doc.txt"
    with open(test_file_path, "w") as f:
        f.write("EchoVision is a sleek AI reading assistant. ")
        f.write("It uses FastAPI, React, and Gemini 1.5. ")
        for i in range(100):
            f.write(f"Filler text for chunking testing sequence {i}. ")
        f.write("The hidden secret password is 'NeonSlime2026'. ")
        
    print("Loading document...")
    ok = dp.load(test_file_path)
    print("Load success:", ok)
    
    print("\n--- Test 1. Normal Query ---")
    query1 = "What technologies does EchoVision use?"
    print(f"Query: {query1}")
    result1 = dp.get_relevant_context(query1, n_results=1)
    print(f"Found Context:\n{result1.strip()}")
    
    print("\n--- Test 2. Secret Query ---")
    query2 = "What is the hidden secret password?"
    print(f"Query: {query2}")
    result2 = dp.get_relevant_context(query2, n_results=1)
    print(f"Found Context:\n{result2.strip()}")
    
    os.remove(test_file_path)

if __name__ == '__main__':
    test_chroma()
