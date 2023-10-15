from erros.ErroEntradaVazia import ErroEntradaVazia
from erros.ErroNaoEncontrado import ErroNaoEncontrado
from modulos.atendimento.EntidadeAtendimento import Atendimento
from modulos.atendimento.TelaAtendimento import TelaAtendimeno
from modulos.mesa.EntidadeMesa import Mesa
from modulos.pedido.ControladorPedido import ControladorPedido


class ControladorAtendimento:
    def __init__(self, controlador_sistema, controlador_pedido: ControladorPedido):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pedido = controlador_pedido
        self.__atendimentos = []
        self.__tela = TelaAtendimeno()
        try:
            self.__carregar_dados()
        except ErroEntradaVazia:
            pass

    @property
    def colecao(self):
        return self.__atendimentos

    @colecao.setter
    def colecao(self, colecao):
        self.__atendimentos = colecao

    def detalhes_atendimento(self, mesa_id: int):
        detalhe = self.__tela.detalhes_atendimento()
        if detalhe["adicionar_pedido"]:
            produtos_pedido = self.__controlador_pedido.criar_pedido()
            print(produtos_pedido)

    def __carregar_dados(self):
        # Busca todos os cadastros e popula a listagem
        result = Atendimento.buscar()
        self.colecao = []
        for dados in result:
            objeto = Atendimento(**dados)
            self.colecao.append(objeto)

    def __buscar_por_id(self, id: int):
        if not len(self.colecao):
            raise ErroEntradaVazia
        try:
            index = [x.id for x in self.colecao].index(id)
        except ValueError:
            raise ErroNaoEncontrado
        objeto = self.colecao[index]
        return (objeto, index)
