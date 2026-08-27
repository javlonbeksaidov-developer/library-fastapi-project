from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db

from .models import Loans


def loan_check(loan_id: int, db: Session = Depends(get_db)):  # noqa: B008
    loan = db.query(Loans).filter(Loans.id == loan_id).first()
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found!"
        )
    return loan
