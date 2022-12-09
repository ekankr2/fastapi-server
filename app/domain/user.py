from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean)
    is_superuser = Column(Boolean)

    posts = relationship('Post', back_populates="creator")
