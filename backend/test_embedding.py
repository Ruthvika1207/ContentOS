print("Starting...")

from services.rag.embeddings import embeddings

print("Embeddings loaded...")

vector = embeddings.embed_query("fitness coaching")

print("Embedding generated!")
print(vector[:5])
print("Length:", len(vector))