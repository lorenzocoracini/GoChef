from modulos.restaurante.EntidadeRestaurante import Restaurante
from modulos.restaurante.TelaRestaurante import TelaRestaurante
from modulos.restaurante.cidade.EntidadeCidadeTeleEntrega import CidadeTeleEntrega


class ControladorRestaurante:
    def __init__(self):
        self.__tela = TelaRestaurante()
        self.__restaurante = None

    def carrega_dados_restaurante(self):
        try:
            self.carregar_dados_restaurante()
            self.carregar_dados_cidades()
        except:
            raise

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

        cidades = [CidadeTeleEntrega(cidade['nome'])
                   for cidade in dados_cidades]
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

    def atualizar_dados_restaurante(self, capacidade_maxima: int):
        self.__restaurante.capacidade_maxima = capacidade_maxima
        self.__restaurante.atualizar()

    def atualizar_cidades(self, novas_cidades):
        cidades_obj = []
        restaurante_id = self.__restaurante.identificador
        for nova_cidade in novas_cidades:
            obj = CidadeTeleEntrega(nova_cidade)
            if obj not in self.__restaurante.cidades:
                obj.guardar(restaurante_id)
                cidades_obj.append(obj)
            else:
                cidades_obj.append(obj)

        for cidade_antiga in self.__restaurante.cidades:
            if cidade_antiga not in cidades_obj:
                cidade_antiga.remover()

        self.__restaurante.cidades = cidades_obj

    def atualizar_dados(self):
        capacidade_maxima_cadastrada = self.__restaurante.capacidade_maxima
        dados = self.__tela.mostra_opcoes(
            'Atualização de dados do restaurante', capacidade_maxima_cadastrada, [
                cidade.nome for cidade in self.__restaurante.cidades])
        self.atualizar_dados_restaurante(dados['capacidade_maxima'])
        self.atualizar_cidades(dados['cidades'])
