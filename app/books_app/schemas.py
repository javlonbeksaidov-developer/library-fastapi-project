from pydantic import BaseModel

from app.authors_app.schemas import AuthorReturn


class BookCreate(BaseModel):
    title: str
    author_id: int
    year: int
    description: str
    quantity: int


class BookReturn(BookCreate):
    id: int
    available_quantity: int
    author: AuthorReturn
