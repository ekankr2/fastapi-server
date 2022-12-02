from sqlalchemy.orm import Session

from app import schemas
from app.domain.user import User


class UserService:
    def create(self, request: schemas.UserCreate, db: Session):
        new_user = User(name=request.name, email=request.email, password=request.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user


user = UserService()
