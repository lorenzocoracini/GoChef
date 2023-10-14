from modulos.produto_pedido.ProdutoPedidoDAO import ProdutoPedidoDAO


class ProdutoPedido(ProdutoPedidoDAO):
    def __init__(self, produto_id: int, quantidade):
        ProdutoPedidoDAO.__init__(self)
        self.__produto_id = produto_id  # Um id Produto
        self.__quantidade = quantidade
        if id is not None:
            self.__id = id

    @property
    def identificador(self) -> int:
        return self.__id

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade: int) -> None:
        self.__quantidade = nova_quantidade

    @property
    def produto_id(self) -> int:
        return self.__produto_id
