from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .models import Authors


def author_check(author_id, db: Session):
    author = db.query(Authors).filter(Authors.id == author_id).first()
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Author not found!"
        )

    return author
