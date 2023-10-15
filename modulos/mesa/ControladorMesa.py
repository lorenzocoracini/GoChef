from erros.ErroEntradaVazia import ErroEntradaVazia
from erros.ErroNaoEncontrado import ErroNaoEncontrado
from erros.ErroValorUnico import ErroValorUnico
from modulos.mesa.EntidadeMesa import Mesa
from modulos.mesa.TelaMesa import TelaMesa
from functools import reduce


class ControladorMesa:
    def __init__(self, controlador_sistema, controlador_atendimento=None):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_atendimento = controlador_atendimento
        self.__mesas = []
        self.__tela = TelaMesa()
        try:
            self.__carregar_dados()
        except ErroEntradaVazia:
            pass

    @property
    def colecao(self):
        return self.__mesas

    @colecao.setter
    def colecao(self, colecao):
        self.__mesas = colecao

    # def mesas_atendidas_e_nao_atendidas(self):
    #     mesas_com_atendimeto = []
    #     mesas_para_inicar_atendimento = []
    #     for mesa in self.colecao:
    #         if mesa.atendimentos != None:
    #             for atendimento in mesa.atendimentos:
    #                 if not atendimento.encerrado:
    #                     mesas_com_atendimeto.append(mesa)
    #                 else:
    #                     mesas_para_inicar_atendimento.append(mesa)
    #     print('--', mesas_com_atendimeto, '--', mesas_para_inicar_atendimento)
    #     return mesas_com_atendimeto, mesas_para_inicar_atendimento

    def listar_mesas(self):
        opcoes = self.__tela.lista_mesas(self.colecao,
                                         self.__controlador_sistema.usuario_atual_eh_gerente)
        if 'adicionar' in opcoes:
            self.cadastrar_mesa()

        if 'atendimento' in opcoes:
            self.detalhes_atendimento(int(opcoes['atendimento']))

        if 'editar' in opcoes:
            self.__editar_mesa(int(opcoes['editar']))

        if 'excluir' in opcoes:
            self.__excluir(int(opcoes['excluir']))
            self.__carregar_dados()

    def cadastrar_mesa(self):
        dados = self.__tela.mostra_formulario()
        if 'voltar' in dados: return
        self.__cadastrar(dados)

    def detalhes_atendimento(self, id):
        self.__controlador_atendimento.detalhes_atendimento(id)

    def __editar_mesa(self, id):
        (mesa, _) = self.__buscar_por_id(id)
        dados = self.__tela.mostra_formulario(
            numero_mesa_cadastrado=mesa.numero_mesa,
            numero_lugares_cadastrado=mesa.numero_lugares
        )

        if 'voltar' in dados: return
        self.__editar(id, dados)

    def __cadastrar(self, dados: dict):
        if self.__ultrapassa_capacidade_maxima(dados['numero_lugares'], self.colecao):
            self.__tela.mostra_mensagem(
                f"O restaurante não tem capacidade suficiente para uma nova mesa com {dados['numero_lugares']} lugares")
            return
        try:
            nova_mesa = Mesa(**dados)
            nova_mesa.guardar()
            self.__carregar_dados()
        except ErroValorUnico:
            self.__tela.mostra_mensagem("Já existe uma mesa com este número de mesa")
        except:
            raise ValueError

    def __ultrapassa_capacidade_maxima(self, numero_lugares, mesas):
        total_numero_lugares = reduce(lambda a, b: a + b.numero_lugares, mesas, 0) + numero_lugares
        return total_numero_lugares > self.__controlador_sistema.lotacao_maxima_restaurante()

    def __editar(self, id, dados: dict):
        try:
            [objeto, _] = self.__buscar_por_id(id)
            if self.__ultrapassa_capacidade_maxima(dados['numero_lugares'],
                                                   list(filter(lambda mesa: mesa.id != id, self.colecao))):
                self.__tela.mostra_mensagem(
                    f"O restaurante não tem capacidade suficiente para uma mesa com {dados['numero_lugares']} lugares")
                return

            atributos_originais = objeto.atributos.items()
            for chave, valor in dados.items():
                setattr(objeto, chave, valor)
            objeto.atualizar()
        except (ErroEntradaVazia, ErroNaoEncontrado):
            raise
        except ErroValorUnico:
            self.__tela.mostra_mensagem("Já existe uma mesa com este número de mesa")
            for chave, valor in atributos_originais:
                if chave != 'id': setattr(objeto, chave, valor)
        except:
            raise ValueError

    def __excluir(self, id):
        try:
            [objeto, _] = self.__buscar_por_id(id)
            if self.__tela.confirma_exclusao_mesa(objeto.numero_mesa):
                objeto.remover()
        except (ErroEntradaVazia, ErroNaoEncontrado):
            raise
        except:
            raise ValueError

    def __carregar_dados(self):
        # Busca todos os cadastros e popula a listagem
        result = Mesa.buscar()
        self.colecao = []
        for dados in result:
            objeto = Mesa(**dados)
            atendimentos = objeto.buscar_atendimentos()
            objeto.atendimentos = atendimentos
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
