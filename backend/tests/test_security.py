from jose import jwt

from api.security import create_access_token
from api.v1.conf.settings import Settings

settings = Settings()  # type: ignore


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert decoded['exp']
