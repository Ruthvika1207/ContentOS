import google.generativeai as genai
from dotenv import load_dotenv
import os

from services.rag.retriever import retrieve_context

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def ask_rag(workspace_id, question):

    docs = retrieve_context(
        workspace_id,
        question
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
    You are a helpful brand knowledge assistant.

    Answer the question using ONLY the provided context.

    Do not use outside knowledge to fill missing information.
    Do not invent facts or product features.

    If the context does not contain the answer,
    say that the information is not available
    in the uploaded brand knowledge.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = model.generate_content(
        prompt
    )

    return response.text