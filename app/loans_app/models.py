from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import relationship

from database import Base


class BookStatus(str, Enum):
    BORROWED = "borrowed"
    RETURNED = "returned"


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