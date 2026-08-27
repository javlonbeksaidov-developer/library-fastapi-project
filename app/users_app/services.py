from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .models import UserRole, Users


def admin_check(admin_id, db: Session):
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found!"
        )
    if admin.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You are not ADMIN!"
        )

    return admin


def admin_or_librarian_check(staff_id, db: Session):
    staff = db.query(Users).filter(Users.id == staff_id).first()
    if not staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if staff.role not in [UserRole.ADMIN, UserRole.LIBRARIAN]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are on the wrong way!",
        )

    return staff


def user_check(user_id, db: Session):
    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
        )

    return user
