from modulos.pedido.PedidoDAO import PedidoDAO
from modulos.produto_pedido.EntidadeProdutoPedido import ProdutoPedido


class Pedido(PedidoDAO):
    def __init__(self):
        PedidoDAO.__init__(self)
        self.__produtos_pedidos: list[ProdutoPedido] = []  # Lista de instancias ProdutoPedido
        if id is not None:
            self.__id = id

    @property
    def identificador(self) -> int:
        return self.__id

    @property
    def produtos_pedidos(self) -> list[int]:
        return self.__produtos_pedidos
