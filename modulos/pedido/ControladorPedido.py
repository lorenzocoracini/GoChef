from modulos.pedido.TelaPedido import TelaPedido
from modulos.pedido.EntidadePedido import Pedido
from modulos.produto_pedido.EntidadeProdutoPedido import ProdutoPedido
from modulos.produto.ControladorProduto import ControladorProduto


class ControladorPedido:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaPedido()
        self.__pedidos = []

    def pega_produtos_cadastrados(self):
        produtos = ControladorProduto(self.__controlador_sistema).pega_dados_produtos()
        return produtos

    def criar_pedido(self):
        produtos = self.pega_produtos_cadastrados()
        pedido = self.__tela.criar_pedido(produtos)

    @property
    def pedidos(self):
        return self.__pedidos

    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos = pedidos
