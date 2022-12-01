from fastapi import APIRouter

from app.schemas.user import UserCreate, UserBase

router = APIRouter()


@router.post('', response_model=UserBase)
def create_user(user_in: UserCreate):

    return 'ok'
