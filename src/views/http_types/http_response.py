# Vamos padronizar as respostas para o usuário
from typing import Dict

class HTTPResponse:
    def __init__(self, status_code: int, body: Dict = None) -> None:
        self.status_code = status_code
        self.body = body
