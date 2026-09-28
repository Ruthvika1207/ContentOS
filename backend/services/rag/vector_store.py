
import os
from pathlib import Path

from langchain_community.vectorstores import FAISS
from services.rag.embeddings import embeddings


# Absolute path to the backend/vectorstores directory
BASE_DIR = Path(__file__).resolve().parents[2]

VECTORSTORE_DIR = BASE_DIR / "vectorstores"


def create_vector_store(chunks, workspace_id):

    path = VECTORSTORE_DIR / str(workspace_id)

    # Create the vectorstores directory if it does not exist
    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if (path / "index.faiss").exists():

        db = FAISS.load_local(
            str(path),
            embeddings,
            allow_dangerous_deserialization=True
        )

        db.add_texts(chunks)

    else:

        db = FAISS.from_texts(
            texts=chunks,
            embedding=embeddings
        )

    # Save the index and document metadata
    db.save_local(str(path))

    print(f"FAISS index saved at: {path}")

    return db


def load_vector_store(workspace_id):

    path = VECTORSTORE_DIR / str(workspace_id)

    index_file = path / "index.faiss"

    if not index_file.exists():

        raise FileNotFoundError(
            f"FAISS index not found for workspace {workspace_id}. "
            f"Expected file: {index_file}. "
            "Please re-upload or reprocess the brand knowledge "
            "document to create the vector store."
        )

    db = FAISS.load_local(
        str(path),
        embeddings,
        allow_dangerous_deserialization=True
    )

    print(f"FAISS index loaded from: {path}")

    return db