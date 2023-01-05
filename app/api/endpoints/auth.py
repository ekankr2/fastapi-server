from datetime import timedelta
from typing import Any

from fastapi import status, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from app import schemas
from app.api import dependencies
from app.core import security
from app.core.config import settings
from app.domain import User
from app.services import user_service, auth_service

router = APIRouter()


@cbv(router)
class AuthController:
    def __init__(self, db: Session = Depends(dependencies.get_db)):
        self.db = db

    @router.post('/register', response_model=schemas.User, status_code=status.HTTP_201_CREATED, summary="User sign up")
    def register(self, request: schemas.UserCreate):
        user = user_service.get_by_email(self.db, email=request.email)
        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this username already exists."
            )
        return user_service.create_user(self.db, request=request)

    @router.post('/login', response_model=schemas.Token, status_code=status.HTTP_200_OK, summary="User Login")
    def login(self, form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
        user = auth_service.authenticate(db=self.db, email=form_data.username, password=form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return {
            "access_token": security.create_access_token(
                user.id, expires_delta=access_token_expires
            ),
            "token_type": "bearer",
        }

    @router.post('/test-token', response_model=schemas.User)
    def test_token(self, current_user: User = Depends(dependencies.get_current_user)):
        return current_user
