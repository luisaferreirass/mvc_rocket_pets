from typing import Dict

# Trocamos informações com o usuário a partiri do protocolo HTTP

class HttpRequest:
    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        self.body = body
        self.param = param

# Vamos pegar as informações da framework e vamos retirar apenas oq vamos utilizar dela
# Sempre que recebemos uma requisição HTTP, o que iremos precisar vai vim na classe HHTPRequest
