from typing import Optional

from sqlalchemy.orm import Session

from app import schemas
from app.domain.user import User


def create_user(request: schemas.UserCreateRequest, db: Session) -> User:
    new_user = User(name=request.name, email=request.email, password=request.password, is_active=request.is_active,
                    is_superuser=request.is_superuser)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_by_email(email: str, db: Session) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()
