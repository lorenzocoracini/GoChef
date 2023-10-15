from modulos.produto_pedido.ProdutoPedidoDAO import ProdutoPedidoDAO


class ProdutoPedido(ProdutoPedidoDAO):
    def __init__(self, produto_id: int, quantidade: int, pedido_id, id=None):
        ProdutoPedidoDAO.__init__(self)
        self.__produto_id = produto_id
        self.__quantidade = quantidade
        self.__pedido_id = pedido_id
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

    @property
    def pedido_id(self) -> int:
        return self.__pedido_id
