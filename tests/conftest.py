import pytest
from fastapi.testclient import TestClient

from backend_tdd_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
