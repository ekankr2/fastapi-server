from sqlalchemy.orm import Session

from app.schemas import UserCreate
from app.services import user_service
from app.tests.utils.utils import random_email, random_lower_string


def test_create_user(db: Session) -> None:
    email = random_email()
    name = 'random_name'
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password, name=name)
    user = user_service.create_user(db, request=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")
