import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table_registry


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session():
    # Cria a conexão com o banco de dados SQLite em memória
    engine = create_engine('sqlite:///:memory:')

    # Cria todas as tabelas definidas no metadata do table_registry
    # no banco de dados conectado
    table_registry.metadata.create_all(engine)

    # Inicia uma nova sessão de banco de dados usando a engine criada
    with Session(engine) as session:
        yield session
        # yield: pausa a execução da fixture, permite a execução do teste,
        # e depois continua para realizar a limpeza.

    # Limpa/destrói todas as tabelas do BD após o teste
    table_registry.metadata.drop_all(engine)
