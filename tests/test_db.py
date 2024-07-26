from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    # Cria uma nova instância do modelo User com os dados fornecidos
    user = User(username='nome', email='nome@mail.com', password='senha')

    # Adiciona a nova instância de User à sessão para que ela seja
    # inserida no banco de dados
    session.add(user)

    # Confirma todas as operações pendentes da sessão,
    # incluindo a inserção do novo usuário
    session.commit()

    # Realiza uma consulta no banco de dados para
    # selecionar o usuário com o email especificado
    result = session.scalar(select(User).where(User.email == 'nome@mail.com'))

    assert result.username == 'nome'
