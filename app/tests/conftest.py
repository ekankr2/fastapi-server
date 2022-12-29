from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.core.config import settings
from app.db.session import SessionLocal
from app.main import app

DATABASE_URI= 'sqlite:///./test.db'


@pytest.fixture(scope="session")
def db() -> Generator:
    test_engine = create_engine(DATABASE_URI, pool_pre_ping=True)
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    Base = declarative_base()
    Base.metadata.create_all(test_engine)
    yield TestSessionLocal()
    Base.metadata.drop_all()

# @pytest.fixture(scope="session")
# def db() -> Generator:
#     yield SessionLocal()

@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


# @pytest.fixture(scope="module")
# def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
#     return authentication_token_from_email(
#         client=client, email=settings.EMAIL_TEST_USER, db=db
#     )
