from modulos.produto.ProdutoDAO import ProdutoDAO

class EntidadeProduto(ProdutoDAO):
    def __init__(self, nome: str, valor: float, id=None) -> None:
        super().__init__()
        self.__nome = nome
        self.__valor = valor
        if id is not None:
            self.__id = id
        
    @property
    def identificador(self):
        return self.__id
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome
    
    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float) -> None:
        self.__valor = valor

    @staticmethod
    def buscar() -> list | None:
        return ProdutoDAO.buscar()