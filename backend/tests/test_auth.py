from freezegun import freeze_time

from api.v1.conf.settings import Settings

settings = Settings()  # type: ignore


def test_token_expiry(client, user):
    with freeze_time('2023-09-28 09:00:00'):
        response = client.post(
            f'{settings.API_VERSION}/token',
            data={'username': user.email, 'password': user.clean_password},
        )

        assert response.status_code == 200
        token = response.json()['access_token']

    with freeze_time('2023-09-28 09:31:00'):
        response = client.post(
            f'{settings.API_VERSION}/refresh_token',
            headers={'Authorization': f'Bearer {token}'},
        )

        assert response.status_code == 401
        assert response.json() == {'detail': 'Could not validate credentials'}


def test_refresh_token(client, user, token):
    response = client.post(
        f'{settings.API_VERSION}/refresh_token',
        headers={'Authorization': f'Bearer {token}'},
    )

    data = response.json()

    assert response.status_code == 200
    assert 'access_token' in data
    assert 'token_type' in data
    assert response.json()['token_type'] == 'bearer'
