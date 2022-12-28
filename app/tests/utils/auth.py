from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.schemas import UserCreate
from app.services import user_service
from app.tests.utils.utils import random_lower_string


# def authentication_token_from_email(
#         *, client: TestClient, email: str, db: Session
# ) -> Dict[str, str]:
#     """
#     Return a valid token for the user with given email.
#
#     If the user doesn't exist it is created first.
#     """
#     password = random_lower_string()
#     user = user_service.get_by_email(db, email=email)
#     if not user:
#         user_in_create = UserCreate(username=email, email=email, password=password)
#         user = user_service.create(db, obj_in=user_in_create)
#     else:
#         user_in_update = UserUpdate(password=password)
#         user = crud.user.update(db, db_obj=user, obj_in=user_in_update)
#
#     return user_authentication_headers(client=client, email=email, password=password)