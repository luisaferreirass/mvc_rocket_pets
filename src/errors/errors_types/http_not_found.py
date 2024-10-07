class HttpNotFoundError(Exception):
# Ela também é uma classe de error e vai ter todas as funcionalidades que o exception tem

    def __init__(self, message: str) -> None:
        super().__init__(message) 
        # Vai conversar com o método construção do exception
        self.status_code = 404
        self.name = "Not Found"
        self.message = message
