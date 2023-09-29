from api.v1.conf.settings import Settings
from api.v1.modules.user.dto.schemas import UserSchemaResponse

settings = Settings()  # type: ignore


def test_create_user(client):
    response = client.post(
        f'{settings.API_VERSION}/users/',
        json={
            'username': 'teste',
            'email': 'teste@example.com',
            'password': '12345678',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'username': 'teste',
        'email': 'teste@example.com',
        'id': 1,
    }


def test_create_user_already_exists(client, user):
    response = client.post(
        f'{settings.API_VERSION}/users/',
        json={
            'username': user.username,
            'email': user.email,
            'password': user.password,
        },
    )

    assert response.status_code == 409
    assert response.json() == {'detail': 'User already exists'}


def test_list_users(client):
    response = client.get(f'{settings.API_VERSION}/users/')

    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_list_users_with_data(client, user):
    user_schema = UserSchemaResponse.model_validate(user).model_dump()
    response = client.get(f'{settings.API_VERSION}/users/')

    assert response.status_code == 200
    assert response.json() == {'users': [user_schema]}


def test_patch_user(client, user, token):
    response = client.patch(
        f'{settings.API_VERSION}/users/{user.id}/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'teste2',
            'email': 'teste2@example.com',
            'password': '12345678',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'username': 'teste2',
        'email': 'teste2@example.com',
        'id': user.id,
    }


def test_not_found_user_patch(client, other_user, token):
    response = client.patch(
        f'{settings.API_VERSION}/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'teste2',
            'email': 'teste2@example.com',
            'password': '12345678',
        },
    )

    assert response.status_code == 401
    assert response.json() == {
        'detail': 'You do not have permission to perform this action'
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'{settings.API_VERSION}/users/{user.id}/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_not_found_user_delete(client, other_user, token):
    response = client.delete(
        f'{settings.API_VERSION}/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 401
    assert response.json() == {
        'detail': 'You do not have permission to perform this action'
    }


def test_get_token(client, user):
    response = client.post(
        f'{settings.API_VERSION}/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_token_invalid_user(client, user):
    response = client.post(
        f'{settings.API_VERSION}/token',
        data={'username': 'teste@email.com', 'password': 'testtest'},
    )
    token = response.json()

    assert response.status_code == 401
    assert token == {'detail': 'Incorrect email or password'}


def test_get_token_invalid_password(client, user):
    response = client.post(
        f'{settings.API_VERSION}/token',
        data={'username': user.email, 'password': 'not_correct_password'},
    )
    token = response.json()

    assert response.status_code == 401
    assert token == {'detail': 'Incorrect email or password'}
