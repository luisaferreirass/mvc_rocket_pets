from src.controllers.interfaces.pet_lister_controller import PetListControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HTTPResponse
from .interfaces.view_interface import ViewInterface

class PetListerView(ViewInterface):
    def __init__(self, controller: PetListControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HTTPResponse:
        body_response = self.__controller.list()
        return HTTPResponse(status_code=200, body=body_response)
