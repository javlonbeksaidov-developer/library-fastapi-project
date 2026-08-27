from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.authors_app.models import Authors
from app.authors_app.schemas import AuthorCreate
from app.users_app.models import Users
from database import get_db

router = APIRouter(tags=["Authors Management"], prefix="/authors")

@router.get("/soon/")
def soon():
    return {"working"}


@router.post("/create-authors/")
def create_authors(user_id: Users, author: AuthorCreate, db: Session = Depends(get_db)):  # noqa: B008
    new_author = Authors(
        name = author.name,
        surname = author.surname,
        bio = author.bio,
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author
