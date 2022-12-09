from fastapi import APIRouter, status

from app.schemas import User, UserCreateRequest
from app.services.user import user_service

router = APIRouter()


@router.post(
    '',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="User sign up",
)
def register(request: UserCreateRequest):
    return user_service.create_user(request)
