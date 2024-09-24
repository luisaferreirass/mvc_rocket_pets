import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler


@pytest.mark.skip(reason="interação com o banco") 
# Estamos falando que não é mais necessário esse teste
def test_connect_to_db(): # Teste de integração com o banco de dados
    assert db_connection_handler.get_engine() is None 
    # Antes de criar o banco, estamos verificando se ele é 
    # realmente none como a gente colocou em default

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    # Estamos verificando se após a conexão com o db, 
    # o motor deixou de ser None
    assert isinstance(db_engine, Engine)
    # Estamos verificando se o nosso engine é realemente um engine
