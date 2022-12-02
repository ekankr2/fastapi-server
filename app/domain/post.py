from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    preview_content = Column(String)
    view = Column(Integer)
    like = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))

    creator = relationship("User", back_populates="posts")
