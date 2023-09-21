import random

from modulos.restaurante.EntidadeRestaurante import Restaurante
from modulos.restaurante.TelaRestaurante import TelaRestaurante
from modulos.restaurante.cidade.EntidadeCidadeTeleEntrega import CidadeTeleEntrega


class ControladorRestaurante:
    def __init__(self):
        self.__tela = TelaRestaurante()
        self.__restaurante = None
        try:
            self.carregar_dados_restaurante()
            self.carregar_dados_cidades()
        except:
            self.cadastrar_dados_iniciais()

    @property
    def restaurante(self):
        return self.__restaurante

    @restaurante.setter
    def restaurante(self, restaurante):
        self.__restaurante = restaurante

    def carregar_dados_restaurante(self) -> None:
        dados_restaurante = Restaurante.buscar()
        if dados_restaurante is None:
            raise Exception

        self.__restaurante = Restaurante(**dados_restaurante)

    def carregar_dados_cidades(self) -> None:
        dados_cidades = CidadeTeleEntrega.buscar()
        if dados_cidades is None:
            raise Exception

        cidades = [CidadeTeleEntrega(cidade) for cidade in dados_cidades]
        self.__restaurante.cidades = cidades

    def cadastrar_dados_iniciais(self):
        dados = self.__tela.mostra_opcoes('Informações do Restaurante')
        novo_restaurante = Restaurante(dados['capacidade_maxima'])
        novo_restaurante.guardar()
        self.carregar_dados_restaurante()
        self.incluir_cidades(
            dados['cidades'], self.__restaurante.identificador)
        self.carregar_dados_cidades()

    def incluir_cidades(self, cidades: list, restaurante_id: int):
        for cidade in cidades:
            nova_cidade = CidadeTeleEntrega(cidade)
            nova_cidade.guardar(restaurante_id)

    def abre_tela():
        pass

#   def editar(self, id, dados: dict, turnos: list):
#     try:
#       [objeto, _] = self.buscar_por_id(id)
#       for chave, valor in dados.items():
#         setattr(objeto, chave, valor)
#       objeto.atualizar()
#       for turno in turnos:
#         turno_editado = Turno(**turno)
#         turno_editado.atualizar()
#     except (ErroEntradaVazia, ErroNaoEncontrado):
#       raise
#     except:
#       raise ValueError

    # def deletar(self, id):
        # try:
        #     [objeto, _] = self.buscar_por_id(id)
        #     objeto.remover()
        #     self.carregar_dados()
        # except ErroNaoEncontrado:
        #     raise ErroNaoEncontrado
        # except:
        #     raise ValueError

    # def cadastrar_turno(self, identificador, turnos):
        # for turno in turnos:
        #     turno["professor"] = identificador
        #     turno["id"] = random.randint(1000, 9999)
        #     novo_turno = Turno(**turno)
        #     novo_turno.guardar()
        #     self.carregar_dados()

    # def deletar_turno(self, id):
        # try:
        #     turno = Turno('', '', 0, 0, id)
        #     turno.remover()
        #     self.carregar_dados()
        # except:
        #     raise ValueError

    # def buscar_por_id(self, id):
        # Recebe um id, busca ele na lista e devolve o objeto e o indice
        # if not len(self.colecao):
        #     raise ErroEntradaVazia
        # try:
        #     index = [x.identificador for x in self.colecao].index(id)
        # except ValueError:
        #     raise ErroNaoEncontrado
        # objeto = self.colecao[index]
        # return (objeto, index)
