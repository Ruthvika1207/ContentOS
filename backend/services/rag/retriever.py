from services.rag.vector_store import load_vector_store

def retrieve_context(workspace_id, query):

    db = load_vector_store(workspace_id)

    docs = db.similarity_search(
        query,
        k=3
    )

    return docs