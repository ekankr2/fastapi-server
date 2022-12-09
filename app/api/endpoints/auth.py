from fastapi import APIRouter

from app.schemas import User, UserCreate
from app.services.user_service import user_service

router = APIRouter()


@router.post('', response_model=User)
def register(request: UserCreate):
    return user_service.create_user(request)
