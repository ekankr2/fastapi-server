from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas
from app.domain import Post
from app.schemas import PostCreate
from app.services.base import BaseService


class PostService(BaseService[Post, PostCreate]):
    def create_post(self, db: Session, request: schemas.PostCreate, user_id: str) -> Post:
        encoded_request = jsonable_encoder(request)
        new_post = Post(**encoded_request, preview_content=request.content[:100], user_id=user_id)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post


post_service = PostService(Post)
