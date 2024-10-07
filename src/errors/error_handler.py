from src.views.http_types.http_response import HTTPResponse
from .errors_types.http_bad_request import HttpBadRequestError
from .errors_types.http_not_found import HttpNotFoundError
from .errors_types.http_unprocessable_entity import HttpUnprocessableEntityError

# vamos retornar uma resposta http
def handle_errors(error: Exception) -> HTTPResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)):
        return HTTPResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    
    return HTTPResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Serever Error",
                "detail": str(error)
            }]
        }
    )
