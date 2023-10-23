from modulos.atendimento.AtendimentoDAO import AtendimentoDAO
from modulos.mesa.EntidadeMesa import Mesa
from modulos.pedido.EntidadePedido import Pedido


class Atendimento(AtendimentoDAO):
    def __init__(self, mesa_id: int, data: str, encerrado: bool, taxa_servico=None, valor_total=None, id=None) -> None:
        AtendimentoDAO.__init__(self)
        if id:
            self.__id = id
        self.__mesa_id = mesa_id
        self.__data = data
        self.__encerrado = encerrado
        self.__taxa_servico = taxa_servico
        self.__valor_total = valor_total
        self.__pedidos: list[Pedido] = []

    @property
    def id(self):
        return self.__id

    @property
    def mesa_id(self):
        return self.__mesa_id

    @mesa_id.setter
    def mesa_id(self, id):
        self.__mesa_id = id

    @property
    def pedidos(self) -> list:
        return self.__pedidos

    @pedidos.setter
    def pedidos(self, value: list):
        self.__pedidos = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def encerrado(self):
        return self.__encerrado

    @encerrado.setter
    def encerrado(self, encerrado):
        self.__encerrado = encerrado

    @property
    def taxa_servico(self):
        return self.__taxa_servico

    @taxa_servico.setter
    def taxa_servico(self, taxa_servico):
        self.__taxa_servico = taxa_servico

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total

    @staticmethod
    def buscar() -> list:
        return AtendimentoDAO.buscar()
