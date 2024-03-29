from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PostBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


# Properties to receive on post create
class PostCreate(PostBase):
    title: str
    content: str


# Properties to return on post delete
class PostDeleteResponse(BaseModel):
    post_id: str
    deleted: bool


class PostInDBBase(PostBase):
    id: Optional[UUID] = None
    preview_content: Optional[str] = None
    view: Optional[int] = None
    like: Optional[int] = None

    class Config:
        orm_mode = True


class Post(PostInDBBase):
    pass
