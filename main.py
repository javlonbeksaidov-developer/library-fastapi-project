from fastapi import FastAPI

from app.models import Base
from app.routes import author_router, book_router, loan_router, user_router
from database import engine

app = FastAPI()
app.include_router(user_router)
app.include_router(author_router)
app.include_router(book_router)
app.include_router(loan_router)


Base.metadata.create_all(engine)


@app.get("/")
def welcome():
    return {"message": "project is working!!!"}
