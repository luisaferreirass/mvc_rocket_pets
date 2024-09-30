from typing import Dict, List
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInteface
from src.models.sqlite.entities.pets import PetsTable

class PetListController:
    def __init__(self, pets_repository: PetsRepositoryInteface) -> None:
        self.__pets_repository = pets_repository
    
    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response


    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pets_repository.list_pets()

        return pets
    

    def __format_response(self, pets: List[PetsTable]) -> Dict:
        formated_pets = [] # estamos colocano a lista de pets em json

        for pet in pets:
            formated_pets.append({
                "name": pet.name,
                "id": pet.id
            })

        return {
            "data": {
                "type": "Pets",
                "count": len(formated_pets),
                "attributes": formated_pets
            }
        }
