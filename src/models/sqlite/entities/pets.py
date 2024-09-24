# Temos que mostrat para o código que a tabela pets existe
from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

#Vamos criar uma imagem do sql script
class PetsTable(Base): # Estamos dizendo que o pets table existe colocando a base como herança
    __tablename__ = 'pets'

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        # quando a gente quiser um elemento dessa tabela, ele vai vim desse jeito
        return f"Pets [name={self.name}, type={self.type}]" 
