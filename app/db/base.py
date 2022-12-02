from sqlalchemy.orm import declarative_base

Base = declarative_base()

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

from app.domain.user import User
from app.domain.post import Post