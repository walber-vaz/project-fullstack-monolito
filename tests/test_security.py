from jose import jwt

from backend_tdd_fastapi.conf.settings import Settings
from backend_tdd_fastapi.security import create_access_token

settings = Settings()  # type: ignore


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']
