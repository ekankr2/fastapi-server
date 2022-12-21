from datetime import timedelta
from typing import Any

from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from app import schemas
from app.core import security
from app.core.config import settings
from app.db.session import get_db
from app.services.user_service import UserService
from app.services.auth_service import AuthService

router = InferringRouter()


@cbv(router)
class AuthController:
    db: Session = Depends(get_db)
    user_service = UserService()
    auth_service = AuthService()

    @router.post('/register', response_model=schemas.User, status_code=status.HTTP_201_CREATED,
                 summary="User sign up")
    def register(self, request: schemas.UserCreateRequest):
        user = self.user_service.get_by_email(self.db, email=request.email)
        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this username already exists."
            )
        return self.user_service.create_user(self.db, request=request)

    # @router.post('/login', response_model=schemas.Token, status_code=status.HTTP_200_OK, summary="User Login")
    # def login(self, form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    #     user = self.auth_service.authenticate(self.session, email=form_data.username, password=form_data.password)
    #     if not user:
    #         raise HTTPException(status_code=400, detail="Incorrect email or password")
    #     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    #     return {
    #         "access_token": security.create_access_token(
    #             user.id, expires_delta=access_token_expires
    #         ),
    #         "token_type": "bearer",
    #     }
