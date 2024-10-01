from .pet_deleter_controller import PetDeleterController


def test_delete_pet(mocker):
    mock_repository = mocker.Mock() 
    # É um mock genérico, ele vai receber todas as informações, mas ele n vai retornar nada
    controller = PetDeleterController(mock_repository)
    controller.delete("amiguinho")
    
    mock_repository.delete_pet.asser_called_once_with("amiguinho")
    # Estamos verificando se estamos chamando o delete com o nome que colocamos
