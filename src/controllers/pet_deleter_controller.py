from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInteface
from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface

class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository:PetsRepositoryInteface) -> None:
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None: # Rotas de deleção não retornam informações
        self.__pet_repository.delete_pets(name)
