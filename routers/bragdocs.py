from fastapi import APIRouter
from pydantic import BaseModel
from services.users import users

router = APIRouter()

class User(BaseModel):
    first_name: str
    last_name: str

@router.post("/create_user")
def create_user(user: User):
    return users.create_user(user.first_name, user.last_name)

@router.get("/get_users")
def get_users():
    return users.get_users()
