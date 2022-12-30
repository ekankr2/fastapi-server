import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Text, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, index=True)
    content = Column(String, index=True)
    preview_content = Column(String, index=True)
    view = Column(Integer, default=0)
    like = Column(Integer, default=0)

    user_id = Column(Text, ForeignKey('user.id'))
    creator = relationship("User", back_populates="posts")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    post_comments = relationship("PostComment", back_populates="parent_post")
