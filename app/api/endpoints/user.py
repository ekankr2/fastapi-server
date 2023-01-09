from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from app import schemas
from app.domain import User
from app.api import dependencies
from app.services import user_service

router = APIRouter()


@cbv(router)
class PostController:
    def __init__(self, db: Session = Depends(dependencies.get_db)):
        self.db = db

    @router.post('/', response_model=schemas.Post, summary="Get User's Written Post.")
    def user_posts(self, current_user: User = Depends(dependencies.get_current_user)):
        return user_service.get_posts_by_user_id(db=self.db, user_id=current_user.id)
