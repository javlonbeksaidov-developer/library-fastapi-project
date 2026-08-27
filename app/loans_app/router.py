from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.books_app.services import book_check
from app.users_app.services import admin_or_librarian_check, user_check
from database import get_db

from .models import BookStatus, Loans
from .schemas import LoanCreate, LoanReturn
from .services import loan_check

router = APIRouter(tags=["Loans Management"], prefix="/loans")

NOW = datetime.now()  # noqa: DTZ005


""" POST """


@router.post("/borrowed/")
def create_loan_borrowed(staff_id: int, loan: LoanCreate, db: Session = Depends(get_db)):  # noqa: B008
    staff = admin_or_librarian_check(staff_id, db)
    new_loan = Loans(
        user_id=loan.user_id,
        book_id=loan.book_id,
        borrowed_at=NOW,
        returned_at=None,
    )

    user_check(loan.user_id, db)

    book = book_check(loan.book_id, db)
    book.available_quantity -= 1
    db.commit()

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return {"message": "created", "user": {"id": staff.id}, "data": new_loan}


@router.patch("/returned/{loan_id}", response_model=list[LoanReturn])
def create_loan_returned(staff_id: int, loan_id: int, db: Session = Depends(get_db)):  # noqa: B008
    staff = admin_or_librarian_check(staff_id, db)
    loan = loan_check(loan_id, db)

    book = book_check(loan.book_id, db)
    book.available_quantity += 1
    loan.returned_at = NOW
    loan.status = BookStatus.RETURNED
    db.commit()
    db.refresh(loan)
    return {"message": "created", "user": {"id": staff.id}, "data": loan}


""" GET """


@router.get("/loans-list/", response_model=list[LoanReturn])
def get_loans_list(staff_id: int, db: Session = Depends(get_db)):  # noqa: B008
    admin_or_librarian_check(staff_id, db)
    loans = db.query(Loans).all()
    return loans


""" DELETE """


@router.delete("/delete/{loan_id}")
def delete_loan(staff_id: int, loan_id: int, db: Session = Depends(get_db)):  # noqa: B008
    staff = admin_or_librarian_check(staff_id, db)
    loan = loan_check(loan_id, db)
    db.delete(loan)
    db.commit()
    return {"message": "deleted", "user": {"id": staff.id}}
