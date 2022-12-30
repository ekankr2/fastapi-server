from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class PostComment(Base):
    __tablename__ = 'post_comment'

    id = Column(Integer, primary_key=True, index=True)
    depth = Column(Integer)
    text = Column(String)

    user_id = Column(Text, ForeignKey('user.id'))
    creator = relationship("User")

    post_id = Column(Text, ForeignKey('post.id'))
    parent_post = relationship("Post", back_populates="post_comments")

