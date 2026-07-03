from services.rag.chunker import chunk_text
from services.rag.vector_store import create_vector_store

from services.rag.rag_chain import ask_rag

text = """
We help working professionals lose fat and improve health.
Our coaching focuses on sustainable weight loss.
We provide personalized fitness plans.
""" * 20

chunks = chunk_text(text)

create_vector_store(chunks)

answer = ask_rag(
    "What services do you provide?"
)

print(answer)