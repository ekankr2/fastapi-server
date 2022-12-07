from fastapi import Depends
from sqlalchemy.orm import Session

from app import schemas
from app.db.session import get_db
from app.domain.user import User


class UserService:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, request: schemas.UserCreate):
        new_user = User(name=request.name, email=request.email, password=request.password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user


user_service = UserService(db=next(get_db()))
