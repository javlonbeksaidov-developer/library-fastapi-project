from pydantic import BaseModel


class AuthorCreate(BaseModel):
    name: str
    surname: str
    bio: str


class AuthorReturn(AuthorCreate):
    id: int
