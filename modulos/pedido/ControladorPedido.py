from erros.ErroEntradaVazia import ErroEntradaVazia
from erros.ErroNaoEncontrado import ErroNaoEncontrado
from modulos.pedido.EntidadePedido import Pedido
from modulos.pedido.TelaPedido import TelaPedido
from modulos.produto.ControladorProduto import ControladorProduto
from modulos.produto_pedido.EntidadeProdutoPedido import ProdutoPedido


class ControladorPedido:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaPedido()
        self.__pedidos = []

    @property
    def colecao(self):
        return self.__pedidos

    @colecao.setter
    def colecao(self, colecao):
        self.__pedidos = colecao

    def pega_produtos_cadastrados(self):
        produtos = ControladorProduto(self.__controlador_sistema).pega_dados_produtos()
        return produtos

    def criar_pedido(self, atendimento_id):
        produtos = self.pega_produtos_cadastrados()
        produtos_do_pedido, event = self.__tela.criar_pedido(produtos)

        pedido_obj = Pedido(atendimento_id=atendimento_id)
        pedido_obj.guardar()

        pedido_id = pedido_obj.identificador

        for produto in produtos_do_pedido:
            produto_id: int = produto['id']
            quantidade: int = produto['quantidade']

            produto_pedido = ProdutoPedido(produto_id, quantidade, pedido_id)
            produto_pedido.guardar()

        self.__carregar_dados()

        return produtos_do_pedido

    def excluir_pedido(self, pedido_id):
        try:
            pedido, _ = self.__buscar_por_id(pedido_id)
            pedido.remover_pedido(pedido_id)
        except (ErroEntradaVazia, ErroNaoEncontrado):
            raise
        except:
            raise ValueError

    def detalhes_do_pedido(self, pedido_id):
        pedido, _ = self.__buscar_por_id(pedido_id)
        prod_ped = pedido.buscar_produtos_pedidos_2(pedido_id)
        print(prod_ped)
        self.__tela.detalhes_do_pedido(prod_ped)

    def __buscar_por_id(self, id: int):
        self.__carregar_dados()
        if not len(self.colecao):
            raise ErroEntradaVazia
        try:
            index = [x["id"] for x in Pedido.buscar()].index(id)
        except ValueError:
            raise ErroNaoEncontrado
        objeto = self.colecao[index]
        return (objeto, index)

    def __carregar_dados(self):
        result = Pedido.buscar()
        self.colecao = []
        for dados in result:
            objeto = Pedido(dados.get('id'))
            produtos_pedidos = objeto.buscar_produtos_pedidos()
            objeto.produtos_pedidos = produtos_pedidos
            self.colecao.append(objeto)
        return self.colecao

    @property
    def pedidos(self):
        return self.__pedidos

    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos = pedidos
