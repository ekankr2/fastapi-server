from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    posts = relationship('Post', back_populates="creator")
