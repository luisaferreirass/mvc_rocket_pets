from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository

# A gente vai usar o mock alchemy como gerente do banco de dados

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data= [
                (
                    [mock.call.query(PetsTable)], #query 
                    [PetsTable(name="dog", type="dog"), 
                    PetsTable(name="cat", type="cat")] # resultado
                    # Se eu fizer uma determinada query, eu vou receber um determinado 
                    # resultado. Estamos definindo o nosso retorno
                )
            ]
        )
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    # Estamos verificando se o query foi chamado no Pets Table
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"
