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

    workspace_data = response.data[0]

    return {
        "message": "Workspace created",
        "workspace_id": workspace_data["id"],
        "workspace": workspace_data
    }

@router.get("/workspace/{user_id}")
def get_workspace(user_id: str):

    response = supabase.table(
        "workspaces"
    ).select("*").eq(
        "user_id",
        user_id
    ).execute()

    if len(response.data) == 0:

        return {
            "exists": False
        }

    return {
        "exists": True,
        "workspace": response.data[0]
    }