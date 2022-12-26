from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PostBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    view: Optional[int] = None
    like: Optional[int] = None


class PostCreate(PostBase):
    title: str
    content: str
    view = 0
    like = 0


class PostInDBBase(PostBase):
    id: Optional[UUID] = None
    preview_content: Optional[str] = None

    class Config:
        orm_mode = True


class Post(PostInDBBase):
    pass
