from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
# Vamos dizer para o pydantic qual o tipo de entrada que vamos aceitar
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError

def person_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        first_name: constr(min_length=1) # type: ignore
        # Não pode ser vazia 
        last_name: constr(min_length=1) # type: ignore
        age: int
        pet_id: int

    try:
        BodyData(**http_request.body)
        # Os dois asteriscos significam que estamos desempacotando tudo do body
        # É a mesma coisa de BpdyData(first_name= "John"...)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
    # Vai retornar todas as informações necessárias de error que nós conseguimos utilizar
