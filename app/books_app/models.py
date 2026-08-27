from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(length=66), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    year = Column(Integer)
    description = Column(Text)
    quantity = Column(Integer, default=0)  # total
    available_quantity = Column(Integer, default=0)  # have library

    author = relationship("Authors", back_populates="book")
    loan = relationship("Loans", back_populates="book")
