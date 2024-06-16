from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_webdev.app import app


def test_read_root_deve_retornar_ok_e_hello_world():

    # Organização do teste (Arrange)
    client = TestClient(app)

    # Ação do teste (Act)
    response = client.get('/')

    # Valida se está funcionando (Assert)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hello world'}
