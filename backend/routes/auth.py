from fastapi import APIRouter
from pydantic import BaseModel
from services.supabase_client import supabase

router = APIRouter()

class UserSignup(BaseModel):
    email: str
    password: str


@router.post("/signup")
def signup(user: UserSignup):

    response = supabase.auth.sign_up({
        "email": user.email,
        "password": user.password
    })

    return {
        "message": "User registered successfully",
        "data": str(response.user.id)
    }

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(user: UserLogin):

    response = supabase.auth.sign_in_with_password(
        {
            "email": user.email,
            "password": user.password
        }
    )

    return {
        "message": "Login successful",
        "access_token": response.session.access_token,
        "user_id": response.user.id
    }