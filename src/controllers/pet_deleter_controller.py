from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInteface


class PetDeleterController:
    def __init__(self, pet_repository:PetsRepositoryInteface) -> None:
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None: # Rotas de deleção não retornam informações
        self.__pet_repository.delete_pets(name)
