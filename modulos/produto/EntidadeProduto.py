from modulos.produto.ProdutoDAO import ProdutoDAO

class Produto(ProdutoDAO):
    def __init__(self, nome: str, valor: float, categoria: int, id=None) -> None:
        super().__init__()
        self.__nome = nome
        self.__valor = valor
        self.__categoria = categoria
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
    def categoria(self) -> int:
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria: int) -> None:
        self.__categoria = categoria
    
    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float) -> None:
        self.__valor = valor
