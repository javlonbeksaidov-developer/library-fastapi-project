from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# DB_URL = "sqlite:///./library.db"
DB_URL = "postgresql://postgres:12345678@localhost:5432/library"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
