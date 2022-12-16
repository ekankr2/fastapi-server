from fastapi import status, Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import User, UserCreateRequest
from app.services import user_service

router = InferringRouter()


@cbv(router)
class AuthController:
    # Notice that Depends() is only callable in the @router functions
    session: Session = Depends(get_db)

    @router.post('/register', response_model=User, status_code=status.HTTP_201_CREATED, summary="User sign up")
    def register(self, request: UserCreateRequest):
        user = user_service.get_by_email(request.email, self.session)
        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this username already exists."
            )
        return user_service.create_user(request, self.session)
