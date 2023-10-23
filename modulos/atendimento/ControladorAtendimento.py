from erros.ErroEntradaVazia import ErroEntradaVazia
from erros.ErroNaoEncontrado import ErroNaoEncontrado
from modulos.atendimento.EntidadeAtendimento import Atendimento
from modulos.atendimento.TelaAtendimento import TelaAtendimento
from modulos.mesa.EntidadeMesa import Mesa
from modulos.pedido.ControladorPedido import ControladorPedido


class ControladorAtendimento:
    def __init__(self, controlador_sistema, controlador_pedido: ControladorPedido):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pedido = controlador_pedido
        self.__atendimentos = []
        self.__tela = TelaAtendimento()
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

    def detalhes_atendimento(self, mesa_id: int, atendimento_id: int, mesa: Mesa):
        if atendimento_id:
            atendimento, _ = self.__buscar_por_id(atendimento_id)
            pedidos = atendimento.pedidos
        else:
            pedidos = []
        detalhe = self.__tela.detalhes_atendimento(pedidos)
        if "adicionar_pedido" in detalhe:
            self.cria_atendimento_e_pedido(mesa_id, mesa, atendimento_id)
        else:
            return

    def cria_atendimento_e_pedido(self, mesa_id, mesa: Mesa, atendimento_id):
        tem_atendimento = self.__ja_tem_atendimento(mesa)
        if not tem_atendimento:
            atendimento = Atendimento(mesa_id=mesa_id, data="12/02/2002", encerrado=False)
            atendimento.guardar()
            dados = self.__carregar_dados()
            id = dados[-1].id
            self.__controlador_pedido.criar_pedido(id)
        else:
            self.__controlador_pedido.criar_pedido(atendimento_id)

    def __ja_tem_atendimento(self, mesa):
        _ja_tem_atendimento = False
        if mesa:
            if mesa.atendimentos:
                _ultimo_atendimento_mesa: Atendimento = mesa.atendimentos[-1]
                if _ultimo_atendimento_mesa["encerrado"] == 0:
                    _ja_tem_atendimento = True
        return _ja_tem_atendimento

    def __carregar_dados(self):
        # Busca todos os cadastros e popula a listagem
        result = Atendimento.buscar()
        self.colecao = []
        for dados in result:
            objeto = Atendimento(**dados)
            pedidos = objeto.buscar_pedidos()
            objeto.pedidos = pedidos
            self.colecao.append(objeto)
        return self.colecao

    def __buscar_por_id(self, id: int):
        if not len(self.colecao):
            raise ErroEntradaVazia
        try:
            dados = self.__carregar_dados()
            index = [x.id for x in dados].index(id)
        except ValueError:
            raise ErroNaoEncontrado
        objeto = dados[index]
        return (objeto, index)
