import pytest
from database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'


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


@pytest.fixture()
def test_client():
    from fastapi.testclient import TestClient
    from main import app
    return TestClient(app)
