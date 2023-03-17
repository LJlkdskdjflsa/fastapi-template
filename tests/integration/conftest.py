import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping():
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'msg': 'pong'}


@pytest.fixture(scope='module')
def test_client():
    with TestClient(app) as test_client:
        yield test_client

