from modulos.pedido.PedidoDAO import PedidoDAO


class Pedido(PedidoDAO):
    def __init__(self):
        PedidoDAO.__init__(self)
        # analisar se vai ser id ou instancia
        self.__produtos_pedidos: list[int] = []  # Lista de ids ProdutoPedido
        if id is not None:
            self.__id = id

    @property
    def identificador(self) -> int:
        return self.__id

    @property
    def produtos_pedidos(self) -> list[int]:
        return self.__produtos_pedidos
