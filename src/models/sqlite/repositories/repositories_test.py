import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# db_connection_handler.connect_to_db() #Estamos se conectando ao banco de dados

@pytest.mark.skip(reason='interacao com o banco')
def test_list_pets(): # Teste de integração (o projeto com o banco)
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)

# Primeiro estamos criando o engine a partir do connect_to_db
# E então a gente cria a instância do repositório e coloca o db_connection_handler como
# argumento de conexão. Quando a gente ativa a função list_pets(), entra no enter do db 
# handler que cria a sessão ativa e retorna o self, que com o with fica como database. 
# Ai procuramos com o database.session a gente consegue entrar dentro do banco de dados
# e fazer o que desejamos

def test_delete_pet():
    name = "belinha"

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)



def test_list_people():
    repo = PeopleRepository(db_connection_handler)
    response = repo.list_people()
    print(response)

    
# Vamos fazer uma conexão fictícia com o ambiente controlado para 
# não ter o contato direto com o banco
# de dados e saber o que nosso códifo está fazendo
