from backend_tdd_fastapi.modules.user.dto.schemas import UserSchemaResponse


def test_create_user(client):
    response = client.post(
        '/users/',
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
        '/users/',
        json={
            'username': user.username,
            'email': user.email,
            'password': user.password,
        },
    )

    assert response.status_code == 409
    assert response.json() == {'detail': 'User already exists'}


def test_list_users(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_list_users_with_data(client, user):
    user_schema = UserSchemaResponse.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {'users': [user_schema]}


def test_patch_user(client, user, token):
    response = client.patch(
        f'/users/{user.id}/',
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
        'id': 1,
    }


def test_not_found_user_patch(client, token):
    response = client.patch(
        '/users/2',
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
        f'/users/{user.id}/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_not_found_user_delete(client, token):
    response = client.delete(
        '/users/2/', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 401
    assert response.json() == {
        'detail': 'You do not have permission to perform this action'
    }


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_token_invalid_user(client, user):
    response = client.post(
        '/token',
        data={'username': 'teste', 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == 401
    assert token == {'detail': 'Incorrect email or password'}


def test_get_token_invalid_password(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': '123456789'},
    )
    token = response.json()

    assert response.status_code == 401
    assert token == {'detail': 'Incorrect email or password'}
