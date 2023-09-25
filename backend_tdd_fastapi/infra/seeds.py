from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from backend_tdd_fastapi.conf.settings import Settings
from backend_tdd_fastapi.modules.user.model.user_model import User
from backend_tdd_fastapi.security import get_password_hash

fake = Faker('pt_BR')
settings = Settings().DATABASE_URL  # type: ignore
engine = create_engine(settings)
session = Session(engine)


def create_user(quantity: int) -> list[User]:
    users = []

    for _ in range(quantity):
        user = User(
            username=fake.name(),
            email=fake.email(),
            password=get_password_hash(fake.password()),
        )

        users.append(user)

    return users


def seed_users(quantity: int) -> None:
    users = create_user(quantity)

    session.add_all(users)
    session.commit()
    session.close()


if __name__ == '__main__':
    seed_users(100)
