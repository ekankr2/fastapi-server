from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import User, UserCreate
from app import services

router = APIRouter()


@router.post('', response_model=User)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return services.user.create(request, db)
