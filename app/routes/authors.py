from fastapi import APIRouter

router = APIRouter(tags=["Authors Management"], prefix="/authors")

@router.get("/soon/")
def soon():
    return {"working"}