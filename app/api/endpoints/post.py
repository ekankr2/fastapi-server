from fastapi import Depends, status, APIRouter
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from app import schemas
from app.core import dependencies
from app.domain import User
from app.services import UserService, PostService

router = APIRouter()


@cbv(router)
class PostController:
    def __init__(self, db: Session = Depends(dependencies.get_db)):
        self.db = db
        self.user_service = UserService()
        self.post_service = PostService()

    @router.post('/', response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
    def create(self, request: schemas.PostCreate, current_user: User = Depends(dependencies.get_current_user)):
        return self.post_service.create_post(db=self.db, request=request, user_id=current_user.id)

