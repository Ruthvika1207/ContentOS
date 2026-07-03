from fastapi import APIRouter

from models.chat import ChatRequest
from services.rag.rag_chain import ask_rag

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    answer = ask_rag(
        request.workspace_id,
        request.question
    )

    return {
        "answer": answer
    }