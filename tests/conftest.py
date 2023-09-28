import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from api.app import app
from api.security import get_password_hash
from api.v1.conf.settings import Settings
from api.v1.infra.database import get_session
from api.v1.modules.user.model.user_model import Base, User

settings = Settings()  # type: ignore


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
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

    app.dependency_overrides.clear()


class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    username = factory.LazyAttribute(lambda o: f'test{o.id}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@test.com')
    password = factory.LazyAttribute(lambda o: f'{o.username}@test.com')


@pytest.fixture
def user(session):
    password = '12345678'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = '12345678'  # type: ignore

    return user


@pytest.fixture
def other_user(session):
    password = 'testtest'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'testtest'  # type: ignore

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        f'{settings.API_VERSION}/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']
