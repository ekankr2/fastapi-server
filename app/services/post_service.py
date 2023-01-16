from fastapi import HTTPException
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

    def delete_post(self, db: Session, post_id: str, user_id: str):
        post_to_delete = self.get_by_id(db, id=post_id)
        if not post_to_delete:
            raise HTTPException(status_code=404, detail="Post not found")
        if not post_to_delete.user_id == user_id:
            raise HTTPException(status_code=404, detail="Not enough permissions to delete this post")

        db.delete(post_to_delete)
        db.commit()

        return {"post_id": post_to_delete.id, "deleted": True}


post_service = PostService(Post)
