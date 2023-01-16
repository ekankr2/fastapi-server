from fastapi.encoders import jsonable_encoder
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


def test_get_user(db: Session):
    email = random_email()
    name = 'random_name'
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password, name=name)
    user = user_service.create_user(db, request=user_in)
    user_2 = user_service.get_by_id(db, id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_get_user_by_email(db: Session):
    email = random_email()
    name = 'random_name'
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password, name=name)
    user = user_service.create_user(db, request=user_in)
    user_2 = user_service.get_by_email(db, email=user.email)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_get_posts_by_user_id(db: Session):
    pass