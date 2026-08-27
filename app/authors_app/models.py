from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Authors(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=50), nullable=False)
    surname = Column(String(length=50), nullable=False)
    bio = Column(Text)

    book = relationship("Books", back_populates="author")
