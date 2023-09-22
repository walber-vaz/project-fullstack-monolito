from fastapi.testclient import TestClient

from backend_tdd_fastapi.app import app


def test_initial_endpoint():
    client = TestClient(app)  # Arrange - Instancia o client
    response = client.get('/')  # Act - Faz a requisição

    assert response.status_code == 200  # Assert - Verifica o resultado
    assert response.json() == {
        'message': 'Olá Mundo!'
    }  # Assert - Verifica o resultado
