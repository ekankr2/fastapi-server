from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.core.config import settings
from app.db.base_class import Base
from app.db.session import SessionLocal
from app.main import app




@pytest.fixture(scope="session")
def engine():
    print("TestCase: Using sqlite database")
    return create_engine("sqlite:///.test.db", echo=False)


@pytest.fixture(scope="session")
def db(engine):
    sessionmaker_ = sessionmaker(bind=engine)
    session = sessionmaker_()
    Base.metadata.create_all(engine)

    yield session

    session.close()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


# @pytest.fixture(scope="module")
# def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
#     return authentication_token_from_email(
#         client=client, email=settings.EMAIL_TEST_USER, db=db
#     )
