import uuid

from sqlalchemy import Column, String, Boolean, DateTime, func, event
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.security import get_password_hash
from app.db.base_class import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    posts = relationship('Post', back_populates="creator")


@event.listens_for(User, "before_insert")
def hash_password(_mapper, _connection, target):
    target.hashed_password = get_password_hash(target.hashed_password)
