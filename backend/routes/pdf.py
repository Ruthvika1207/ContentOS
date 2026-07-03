from fastapi import APIRouter, UploadFile, File, Form

from services.pdf.pdf_reader import extract_text_from_pdf
from services.rag.chunker import chunk_text
from services.rag.vector_store import create_vector_store
from services.supabase_client import supabase

router = APIRouter()


@router.post("/upload-pdf")
async def upload_pdf(
    workspace_id: str = Form(...),
    file: UploadFile = File(...)
):

    print("Filename:", file.filename)

    text = extract_text_from_pdf(file.file)

    print("Text Length:", len(text))

    data = {
        "workspace_id": workspace_id,
        "filename": file.filename,
        "content": text
    }

    print("Data being inserted:", data)

    response = supabase.table(
        "brand_documents"
    ).insert(data).execute()

    print(response)

    chunks = chunk_text(text)
    create_vector_store(chunks, workspace_id)

    return {
        "message": "PDF processed successfully"
    }