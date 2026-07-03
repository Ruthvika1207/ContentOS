from services.rag.chunker import chunk_text
from services.rag.vector_store import create_vector_store

sample_text = """
We help working professionals lose fat and build sustainable fitness habits.
Our coaching focuses on nutrition and long term health.
""" * 20

chunks = chunk_text(sample_text)

db = create_vector_store(chunks)

print("FAISS Created Successfully")