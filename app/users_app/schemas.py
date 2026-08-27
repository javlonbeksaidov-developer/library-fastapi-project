from pydantic import BaseModel

from .models import UserRole

""" USER """


class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str


class UserReturn(BaseModel):
    id: int
    username: str
    password: str
    full_name: str
    role: UserRole
    status: bool
