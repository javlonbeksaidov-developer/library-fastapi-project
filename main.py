from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.authors_app import Authors, author_router  # noqa: F401
from app.books_app import Books, book_router  # noqa: F401
from app.loans_app import Loans, loan_router  # noqa: F401
from app.users_app import Users, user_router  # noqa: F401
from database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Dastur ishga tushganda barcha jadvallar yaratiladi
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Library Management API", lifespan=lifespan)
""" ROUTERS """
app.include_router(user_router)
app.include_router(author_router)
app.include_router(book_router)
app.include_router(loan_router)


@app.get("/")
def welcome():
    return {"message": "project is working!!!"}
