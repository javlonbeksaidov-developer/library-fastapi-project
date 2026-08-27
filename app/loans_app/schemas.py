from datetime import datetime

from pydantic import BaseModel

from app.books_app.schemas import BookReturn
from app.users_app.schemas import UserReturn

from .models import BookStatus


class LoanCreate(BaseModel):
    user_id: int
    book_id: int


class LoanReturn(BaseModel):
    id: int
    borrowed_at: datetime | None = None
    returned_at: datetime | None = None
    status: BookStatus
    user: UserReturn
    book: BookReturn
