from services.rag.chunker import chunk_text
from services.rag.vector_store import create_vector_store
from services.rag.retriever import retrieve_context

text = """
We help working professionals lose fat and improve health.
Our coaching focuses on sustainable weight loss.
""" * 20

chunks = chunk_text(text)

create_vector_store(chunks)

results = retrieve_context(
    "How do I lose weight?"
)

for r in results:
    print(r.page_content)