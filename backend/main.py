from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.workspace import router as workspace_router
from routes.document import router as document_router
from routes.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
from routes.pdf import router as pdf_router
from routes.research import router as research_router
from routes.strategy import router as strategy_router
from routes.writer import router as writer_router
from routes.workflow import (
    router as workflow_router
)
from routes.publish import router as publish_router
from routes.campaign import router as campaign_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pdf_router)
app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(workspace_router)
app.include_router(document_router)
app.include_router(research_router)
app.include_router(strategy_router)
app.include_router(writer_router)
app.include_router(
    workflow_router
)
app.include_router(
    publish_router
)
app.include_router(
    campaign_router
)

@app.get("/")
def home():
    return {"message": "ContentOS Backend Running"}