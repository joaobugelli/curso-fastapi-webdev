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


def test_delet_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
