from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_world(client):
    # Ação do teste (Act)
    response = client.get('/')

    # Valida se está funcionando (Assert)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hello world'}


def test_create_user(client):
    # Captura a response do post
    response = client.post(
        '/users/',
        json={
            'username': 'nome',
            'password': 'senha',
            'email': 'nome@mail.com',
        },
    )

    # Retorna o status code correto
    assert response.status_code == HTTPStatus.CREATED

    # Validar UserPublic
    assert response.json() == {
        'username': 'nome',
        'email': 'nome@mail.com',
        'id': 1,
    }


def test_read_users(client):
    # Captura a response do get
    response = client.get('/users')

    # Valida status code
    assert response.status_code == HTTPStatus.OK

    # Valida UserList
    assert response.json() == {
        'users': [
            {
                'username': 'nome',
                'email': 'nome@mail.com',
                'id': 1,
            }
        ]
    }


def test_read_user_by_id(client):
    # Captura a response do get de um user específico
    response = client.get('/users/1')

    # Valida status code
    assert response.status_code == HTTPStatus.OK

    # Valida response
    assert response.json() == {
        'username': 'nome',
        'email': 'nome@mail.com',
        'id': 1,
    }


def test_read_user_by_id_not_found(client):
    # Captura a response do put (not found)
    response = client.get('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(client):
    # Captura a response do put
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'novo nome',
            'email': 'nome@mail.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'novo nome',
        'email': 'nome@mail.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    # Captura a response do put (not found)
    response = client.put(
        '/users/999',
        json={
            'password': '123',
            'username': 'novo nome',
            'email': 'nome@mail.com',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delet_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    # Captura a response do delete (not found)
    response = client.delete('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
