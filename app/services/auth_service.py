from typing import Optional

from sqlalchemy.orm import Session

from app.domain.user import User
from .user_service import user_service
from ..core.security import verify_password


class AuthService:

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        user = user_service.get_by_email(db=db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


auth_service = AuthService()
