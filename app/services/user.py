from fastapi import Depends
from sqlalchemy.orm import Session

from app import schemas
from app.db.session import get_db
from app.domain.user import User


class UserService:

    def create_user(self, request: schemas.UserCreateRequest, db: Session) -> User:
        new_user = User(name=request.name, email=request.email, password=request.password, is_active=request.is_active,
                        is_superuser=request.is_superuser)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
