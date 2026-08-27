from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.users_app.services import admin_or_librarian_check
from database import get_db

from .models import Authors
from .schemas import AuthorCreate, AuthorReturn
from .services import author_check

router = APIRouter(tags=["Authors Management"], prefix="/authors")

""" POST """


@router.post("/create-authors/")
def create_authors(staff_id: int, author: AuthorCreate, db: Session = Depends(get_db)):  # noqa: B008
    staff = admin_or_librarian_check(staff_id, db)  # Huquq tekshiruvi
    print(staff)

    new_author = Authors(
        name=author.name,
        surname=author.surname,
        bio=author.bio,
    )
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return {"message": "Created", "user": {"id": staff.id}, "data": new_author}


""" GET """


@router.get("/authors-list/", response_model=list[AuthorReturn])
def get_authors_list(db: Session = Depends(get_db)):  # noqa: B008
    authors = db.query(Authors).all()
    return authors


@router.get("/author/{author_id}", response_model=AuthorReturn)
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):  # noqa: B008
    author = db.query(Authors).filter(Authors.id == author_id).first()
    return author


""" DELETE """


@router.delete("/delete/{author_id}")
def delete_author(staff_id: int, author_id: int, db: Session = Depends(get_db)):  # noqa: B008
    staff = admin_or_librarian_check(staff_id, db)  # Huquq tekshiruvi
    author = author_check(author_id, db)
    db.delete(author)
    db.commit()
    return {"message": "Deleted", "user": staff}
