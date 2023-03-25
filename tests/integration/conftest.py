import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
from app.main import app

client = TestClient(app)


@pytest.fixture(scope='module')
def test_client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope='function')
def in_memory_db_engine():
    # create in memory sqlite engine
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False},
    )
    # create all table for this session
    Base.metadata.create_all(bind=engine)
    return engine


@pytest.fixture(scope='function')
def fake_session(in_memory_db_engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=in_memory_db_engine)
