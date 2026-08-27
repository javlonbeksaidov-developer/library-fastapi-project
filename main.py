from fastapi import FastAPI

from app.authors_app import Authors, author_router  # noqa: F401
from app.books_app import Books, book_router  # noqa: F401
from app.loans_app import Loans, loan_router  # noqa: F401
from app.users_app import Users, user_router  # noqa: F401
from database import Base, engine

app = FastAPI()
""" ROUTERS """
app.include_router(user_router)
app.include_router(author_router)
app.include_router(book_router)
app.include_router(loan_router)


Base.metadata.create_all(engine)


@app.get("/")
def welcome():
    return {"message": "project is working!!!"}
