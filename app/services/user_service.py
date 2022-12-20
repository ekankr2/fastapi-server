from typing import Optional

from sqlalchemy.orm import Session

from app import schemas
from app.domain.user import User


class UserService:
    def create_user(self, db: Session, request: schemas.UserCreateRequest) -> User:
        new_user = User(name=request.name, email=request.email, hashed_password=request.password,
                        is_active=request.is_active, is_superuser=request.is_superuser)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
