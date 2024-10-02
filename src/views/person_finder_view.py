from src.controllers.interfaces.person_finder_controller import PersonFinderControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HTTPResponse

class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HTTPResponse:
        person_id = http_request.param["person_id"]
        body_response = self.__controller.find(person_id)

        return HTTPResponse(status_code= 200, body= body_response)
