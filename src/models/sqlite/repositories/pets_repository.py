from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInteface

class PetsRepository(PetsRepositoryInteface): # Essa classe de repositório vai depender da conexão
    def __init__(self, db_connection) -> None:
        # Vamos definir a conexão desejada
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all() 
                # Como estamos retornando o self com o enter a gente consegue usar o session
                return pets
            except NoResultFound:
                return []
            
    def delete_pets(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                database.session
                .query(PetsTable)
                .filter(PetsTable.name == name)
                .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback() 
                # Se der qualquer erro, quero que vc volte o banco para como ele estava sem 
                #fazer a deleção e levante a mesma exceção que estava aqui
                raise exception
