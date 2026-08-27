from fastapi import APIRouter

router = APIRouter(tags=["Loans Management"], prefix="/loans")

@router.get("/soon/")
def soon():
    return {"working"}