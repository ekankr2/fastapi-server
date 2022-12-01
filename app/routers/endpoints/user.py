from fastapi import APIRouter

from app.schemas import User, UserCreate

router = APIRouter()


@router.post('', response_model=User)
def create_user(user_in: UserCreate):

    return 'ok'
