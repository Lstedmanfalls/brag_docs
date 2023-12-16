from fastapi import APIRouter
from services import get_service

router = APIRouter()


@router.get("/")
def service():
    new_service = get_service.GetService()
    return (new_service.get_service())
