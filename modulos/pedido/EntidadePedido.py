import uuid

from modulos.pedido.PedidoDAO import PedidoDAO
from modulos.produto_pedido.EntidadeProdutoPedido import ProdutoPedido


class Pedido(PedidoDAO):
    def __init__(self, atendimento_id: int, id=None):
        super().__init__()
        self.__id = id if id else self.__gerar_id()
        self.__atendimento_id = atendimento_id
        self.__produtos_pedidos: list[ProdutoPedido] = []  # Lista de instancias ProdutoPedido

    def __gerar_id(self):
        return str(uuid.uuid4())

    @property
    def identificador(self) -> int:
        return self.__id

    @property
    def atendimento_id(self):
        return self.__atendimento_id

    @atendimento_id.setter
    def atendimento_id(self, id):
        self.__atendimento_id = id

    @property
    def produtos_pedidos(self) -> list:
        return self.__produtos_pedidos

    @produtos_pedidos.setter
    def produtos_pedidos(self, value):
        self.__produtos_pedidos = value
