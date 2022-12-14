from fastapi import status, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import User, UserCreateRequest
from app.services.user import UserService


router = InferringRouter()


@cbv(router)
class AuthController:
    session: Session = Depends(get_db)
    user_service = UserService()

    @router.post(
        '/',
        response_model=User,
        status_code=status.HTTP_201_CREATED,
        summary="User sign up",
    )
    def register(self, request: UserCreateRequest):
        return self.user_service.create_user(request, self.session)
