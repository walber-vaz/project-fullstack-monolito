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


def test_patch_user(client, user):
    response = client.patch(
        '/users/1',
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


def test_not_found_user_patch(client):
    response = client.patch(
        '/users/2',
        json={
            'username': 'teste2',
            'email': 'teste2@example.com',
            'password': '12345678',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_not_found_user_delete(client):
    response = client.delete('/users/2')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
