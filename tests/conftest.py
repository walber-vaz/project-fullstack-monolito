import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend_tdd_fastapi.app import app
from backend_tdd_fastapi.infra.database import get_session
from backend_tdd_fastapi.modules.user.model.user_model import Base, User


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides = {}


@pytest.fixture
def user(session):
    user = User(
        username='test',
        email='test@email.com',
        password='test12345678',
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
