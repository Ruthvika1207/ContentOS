from fastapi import APIRouter
from models.document import DocumentCreate
from services.supabase_client import supabase

from services.rag.chunker import chunk_text
from services.rag.vector_store import create_vector_store

router = APIRouter()

@router.post("/documents")
def create_document(document: DocumentCreate):

    response = supabase.table(
        "brand_documents"
    ).insert(
        {
            "workspace_id": document.workspace_id,
            "content": document.content
        }
    ).execute()

    chunks = chunk_text(
        document.content
    )

    create_vector_store(
        chunks,
        document.workspace_id
    )

    return {
        "message": "Document stored and indexed",
        "data": response.data
    }


@router.get("/documents/{workspace_id}")
def get_documents(workspace_id: str):

    response = supabase.table(
        "brand_documents"
    ).select("*").eq(
        "workspace_id",
        workspace_id
    ).execute()

    return response.data


@router.delete("/documents/{document_id}")
def delete_document(document_id: str):

    response = supabase.table(
        "brand_documents"
    ).delete().eq(
        "id",
        document_id
    ).execute()

    return {
        "message": "Document deleted successfully"
    }