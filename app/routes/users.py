from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import UserRole, Users
from app.schemas import UserCreate, UserReturn
from database import get_db

router = APIRouter(tags=["Users Management"], prefix="/users")


def admin_check(admin_id, db: Session):
    admin = db.query(Users).filter(Users.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    if admin.role != UserRole.ADMIN:
        raise HTTPException(status_code=401, detail="Not Admin")

    return admin


def user_check(user_id, db: Session):
    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


""" POST """


@router.post("/create-admin/", response_model=UserReturn)
def create_admin(user: UserCreate, db: Session = Depends(get_db)):
    admin = Users(
        username=user.username,
        password=user.password,
        full_name=user.full_name,
        role=UserRole.ADMIN,
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin


@router.post("/create-user/", response_model=UserReturn)
def create_user(admin_id: int, user: UserCreate, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    users = Users(
        username=user.username,
        password=user.password,
        full_name=user.full_name,
    )
    db.add(users)
    db.commit()
    db.refresh(users)
    return users


@router.post("/create-librarian/", response_model=UserReturn)
def create_librarian(admin_id: int, user: UserCreate, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    users = Users(
        username=user.username,
        password=user.password,
        full_name=user.full_name,
        role=UserRole.LIBRARIAN,
    )
    db.add(users)
    db.commit()
    db.refresh(users)
    return users


""" GET """


@router.get("/users-list/", response_model=list[UserReturn])
def get_users(admin_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    users = db.query(Users).all()
    return users


@router.get("/admins/", response_model=list[UserReturn])
def get_all_admins(admin_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    admin = db.query(Users).filter(Users.role == "ADMIN").all()
    return admin


@router.get("/librarians/", response_model=list[UserReturn])
def get_all_librarians(admin_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    librarian = db.query(Users).filter(Users.role == "LIBRARIAN").all()
    return librarian


@router.get("/users/", response_model=list[UserReturn])
def get_all_users(admin_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    user = db.query(Users).filter(Users.role == "USER").all()
    return user


""" DELETE """


@router.delete("/delete-user/{user_id}")
def delete_user(admin_id: int, user_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    user = user_check(user_id, db)

    db.delete(user)
    db.commit()
    return {"message": "Deleted user from data."}


""" PATCH | USER """


@router.patch("/user-to-admin/")
def user_to_admin(admin_id: int, user_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    user = user_check(user_id, db)

    user.role = UserRole.ADMIN
    db.commit()
    db.refresh(user)
    return {"message": "user to admin", "data": user}


@router.patch("/user-to-librarian/")
def user_to_librarian(admin_id: int, user_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    user = user_check(user_id, db)

    user.role = UserRole.LIBRARIAN
    db.commit()
    db.refresh(user)
    return {"message": "user to librarian", "data": user}


""" PATCH | LIBRARIAN """


@router.patch("/librarian-to-admin/")
def librarian_to_admin(admin_id: int, user_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    user = user_check(user_id, db)

    user.role = UserRole.ADMIN
    db.commit()
    db.refresh(user)
    return {"message": "librarian to admin", "data": user}


@router.patch("/librarian-to-user/")
def librarian_to_user(admin_id: int, user_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    user = user_check(user_id, db)

    user.role = UserRole.USER
    db.commit()
    db.refresh(user)
    return {"message": "librarian to user", "data": user}


""" PATCH | ADMIN """


@router.patch("/admin-to-user/")
def admin_to_user(admin_id: int, user_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    user = user_check(user_id, db)

    user.role = UserRole.USER
    db.commit()
    db.refresh(user)
    return {"message": "admin to user", "data": user}


@router.patch("/admin-to-librarian/")
def admin_to_librarian(admin_id: int, user_id: int, db: Session = Depends(get_db)):
    admin_check(admin_id, db)

    user = user_check(user_id, db)

    user.role = UserRole.LIBRARIAN
    db.commit()
    db.refresh(user)
    return {"message": "admin to librarian", "data": user}
