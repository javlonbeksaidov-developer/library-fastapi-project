from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db

from .models import Books


def book_check(book_id: int, db: Session = Depends(get_db)):  # noqa: B008
    book = db.query(Books).filter(Books.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!"
        )

    return book
