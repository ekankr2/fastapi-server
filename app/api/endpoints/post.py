from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import User, UserCreateRequest
from app.services.user_service import user_service

router = APIRouter()


@router.post('', response_model=User)
def create(request: UserCreateRequest, db: Session = Depends(get_db)):
    return user_service.create_user(request, db)
