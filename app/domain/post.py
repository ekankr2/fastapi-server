from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    preview_content = Column(String, index=True)
    view = Column(Integer, default=0)
    like = Column(Integer, default=0)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))

    creator = relationship("User", back_populates="posts")
