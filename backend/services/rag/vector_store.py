import os

from langchain_community.vectorstores import FAISS
from services.rag.embeddings import embeddings


def create_vector_store(chunks, workspace_id):

    path = f"vectorstores/{workspace_id}"

    if os.path.exists(path):

        db = FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True
        )

        db.add_texts(chunks)

    else:

        db = FAISS.from_texts(
            texts=chunks,
            embedding=embeddings
        )

    db.save_local(path)

    return db


def load_vector_store(workspace_id):

    return FAISS.load_local(
        f"vectorstores/{workspace_id}",
        embeddings,
        allow_dangerous_deserialization=True
    )