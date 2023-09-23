from sqlalchemy import select

from backend_tdd_fastapi.modules.user.model.user_model import User


def test_get_user(session):
    new_user = User(username='test', password='test', email='email@email.com')
    session.add(new_user)
    session.commit()

    stmt = session.scalar(select(User).where(User.username == 'test'))

    assert stmt.username == 'test'
