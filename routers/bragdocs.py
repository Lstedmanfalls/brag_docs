from fastapi import APIRouter

router = APIRouter()

@router.get("/hi")
def get_root():
    return "hello I am a bragdocs endpoint"