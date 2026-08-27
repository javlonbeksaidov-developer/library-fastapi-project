from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.users_app.services import admin_or_librarian_check
from database import get_db

from .models import Books
from .schemas import BookCreate, BookReturn
from .services import book_check

router = APIRouter(tags=["Books Management"], prefix="/books")


""" POST """


@router.post("/create-book/")
def create_book(staff_id: int, book: BookCreate, db: Session = Depends(get_db)):  # noqa: B008
    staff = admin_or_librarian_check(staff_id, db)
    new_book = Books(
        title=book.title,
        author_id=book.author_id,
        year=book.year,
        description=book.description,
        quantity=book.quantity,
        available_quantity=book.quantity,
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"message": "created", "user": {"id": staff.id}, "data": new_book}


""" GET """


@router.get("/books-list/", response_model=list[BookReturn])
def get_books_list(db: Session = Depends(get_db)):  # noqa: B008
    books = db.query(Books).all()
    return books


@router.get("/book/{book_id}", response_model=BookReturn)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):  # noqa: B008
    book = book_check(book_id, db)
    return book


""" DELETE """


@router.delete("/delete/{book_id}")
def delete_book(staff_id: int, book_id: int, db: Session = Depends(get_db)):  # noqa: B008
    staff = admin_or_librarian_check(staff_id, db)
    book = book_check(book_id, db)
    db.delete(book)
    db.commit()
    return {"message": "deleted", "user": {"id": staff.id}}
