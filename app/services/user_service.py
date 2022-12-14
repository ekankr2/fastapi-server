from typing import Optional

from sqlalchemy.orm import Session, joinedload

from app import schemas
from app.domain.user import User
from app.schemas import UserCreate
from app.services.base import BaseService


class UserService(BaseService[User, UserCreate]):
    def create_user(self, db: Session, request: schemas.UserCreate) -> User:
        new_user = User(name=request.name, email=request.email, hashed_password=request.password,
                        is_active=request.is_active, is_superuser=request.is_superuser)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_posts_by_user_id(self, db: Session, user_id: str):
        return db.query(User).options(joinedload(User.posts)).filter(User.id == user_id).all()


user_service = UserService(User)
