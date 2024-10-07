from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HTTPResponse
from .interfaces.view_interface import ViewInterface

class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HTTPResponse:
        name = http_request.param["name"]
        self.__controller.delete(name)

        return HTTPResponse(status_code= 204)
