from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class PostComment(Base):
    __tablename__ = 'post_comment'

    id = Column(Integer, primary_key=True, index=True)
    depth = Column(Integer)
    text = Column(String)

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    creator = relationship("User", back_populates="comments")

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", back_populates="comments")

