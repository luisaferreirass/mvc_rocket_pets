"""
exc_type: O tipo da exceção que ocorreu, se houver.
        Se não ocorreu nenhuma exceção, este parâmetro será None.

exc_val: O valor da exceção que ocorreu, se houver.
        Se não ocorreu nenhuma exceção, este parâmetro será None.

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu, se houver.
(a memória de dados dos erros que aconteceram) 
        Se não ocorreu nenhuma exceção, este parâmetro será None.
"""

class AlgumaCoisa:
    def __enter__(self):
        print("estou entrando") #Assim que entrarmos no with o enter vai rodar

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("estou saindo") #Assim que sairmos do bloco with o exit vai rodar



with AlgumaCoisa() as Something:
    print("Estou no meio")

# Esse métodos nos ajudam a reger conexões e métodos de conexões
