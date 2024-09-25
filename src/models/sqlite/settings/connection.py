from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):   
        # Estamos criando um motor para se conectar ao banco de dados a partir de uma conexão ativa     
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine) # Vou ter a sessão a partir do nosso engine
        return self # Retornando o contexto da nossa classe 
                    # para podermos usar o session no bloco with

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close() #Estamos fechando a sessão

db_connection_handler = DBConnectionHandler()

#Vamos estabelecer a conexão agora
