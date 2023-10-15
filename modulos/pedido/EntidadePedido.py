from modulos.pedido.PedidoDAO import PedidoDAO
from modulos.produto_pedido.EntidadeProdutoPedido import ProdutoPedido


class Pedido(PedidoDAO):
    proximo_id = 1

    def __init__(self):
        super().__init__()
        self.__id = Pedido.proximo_id
        self.__produtos_pedidos: list[ProdutoPedido] = []  # Lista de instancias ProdutoPedido
        Pedido.proximo_id += 1

    @property
    def identificador(self) -> int:
        return self.__id

    @property
    def produtos_pedidos(self) -> list[int]:
        return self.__produtos_pedidos
