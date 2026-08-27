from fastapi import APIRouter

router = APIRouter(tags=["Books Management"], prefix="/books")

@router.get("/soon/")
def soon():
    return {"working"}