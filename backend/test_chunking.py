from services.rag.chunker import chunk_text

sample_text = """
We help working professionals lose fat and build sustainable fitness habits.
Our coaching focuses on nutrition, exercise, and long-term health.
""" * 20

chunks = chunk_text(sample_text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk[:100])