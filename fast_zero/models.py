from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

# registry = registra os metadados da tabela
# Mapped = define qual tipo de variável será mapeado no python

table_registry = registry()


@table_registry.mapped_as_dataclass  # classe de dados não tem métodos
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    # init define que o campo não será preenchido ao criar uma instancia
    # primary key define que esse campo será a chave primária da tabela
    # por padrão a PK já vai incrementar +1 quando receber um novo registro
    username: Mapped[str] = mapped_column(unique=True)
    # unique: o BD valida se tem outro registro com o mesmo username
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
