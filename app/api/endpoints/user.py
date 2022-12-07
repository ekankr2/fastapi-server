from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import User, UserCreate
from app.services.user_service import user_service

router = APIRouter()


@router.post('', response_model=User)
def create_user(request: UserCreate):
    return user_service.create_user(request)
