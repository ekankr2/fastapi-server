from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas
from app.domain import Post


class PostService:
    def create_post(self, db: Session, request: schemas.PostCreate, user_id: str) -> Post:
        obj_in_data = jsonable_encoder(request)
        new_post = Post(**obj_in_data, preview_content=request.content[:100], user_id=user_id)
        return new_post
