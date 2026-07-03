from fastapi import APIRouter
from models.workspace import WorkspaceCreate
from services.supabase_client import supabase

router = APIRouter()

@router.post("/workspace")

def create_workspace(workspace: WorkspaceCreate):

    response = supabase.table(
        "workspaces"
    ).insert(
        {
            "user_id": workspace.user_id,
            "name": workspace.name,
            "description": workspace.description
        }
    ).execute()

    return {
        "message":"Workspace created",
        "data":response.data
    }