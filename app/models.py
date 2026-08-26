from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship

from database import Base


class UserRole(str, Enum):
    ADMIN = "admin"
    LIBRARIAN = "librarian"
    USER = "user"


class BookStatus(str, Enum):
    BORROWED = "borrowed"
    RETURNED = "returned"


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(length=66), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)
    full_name = Column(String(length=100), nullable=False)
    role = Column(SQLEnum(UserRole), default=UserRole.USER)
    status = Column(Boolean, default=True, nullable=False)

    loan = relationship("Loans", back_populates="user")


class Authors(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=50), nullable=False)
    surname = Column(String(length=50), nullable=False)
    bio = Column(Text)

    book = relationship("Books", back_populates="author")


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(length=66), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    year = Column(Integer)
    quantity = Column(Integer, default=0)
    available_quantity = Column(Integer, default=0)
    status = Column(Boolean, default=True)

    author = relationship("Authors", back_populates="book")
    loan = relationship("Loans", back_populates="book")


class Loans(Base):  # Kitobni kim olganini saqlaydi.
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    borrowed_at = Column(DateTime, default=datetime.now)
    returned_at = Column(DateTime, default=None)
    status = Column(SQLEnum(BookStatus), default=BookStatus.BORROWED, nullable=False)

    user = relationship("Users", back_populates="loan")
    book = relationship("Books", back_populates="loan")
