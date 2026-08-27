
from enum import Enum

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship

from database import Base


class UserRole(str, Enum):
    ADMIN = "admin"
    LIBRARIAN = "librarian"
    USER = "user"


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(length=66), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)
    full_name = Column(String(length=100), nullable=False)
    role = Column(SQLEnum(UserRole), default=UserRole.USER)
    status = Column(Boolean, default=True, nullable=False)

    loan = relationship("Loans", back_populates="user")