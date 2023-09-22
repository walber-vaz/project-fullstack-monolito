from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
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


def test_list_users(client: TestClient):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'username': 'teste',
                'email': 'teste@example.com',
                'id': 1,
            }
        ]
    }


def test_patch_user(client: TestClient):
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


def test_not_found_user_patch(client: TestClient):
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


def test_delete_user(client: TestClient):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_not_found_user_delete(client: TestClient):
    response = client.delete('/users/2')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
