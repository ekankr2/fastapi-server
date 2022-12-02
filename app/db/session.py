from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base

SQLALCHAMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)