from modulos.restaurante.RestauranteDAO import RestauranteDAO
from modulos.restaurante.cidade.EntidadeCidadeTeleEntrega import CidadeTeleEntrega


class Restaurante(RestauranteDAO):
    def __init__(self, capacidade_maxima: int, id=None) -> None:
        super().__init__()
        if id is not None:
            self.__id = id
        self.__capacidade_maxima = capacidade_maxima
        self.__cidades = None

    @property
    def identificador(self) -> int:
        return self.__id

    @property
    def capacidade_maxima(self) -> int:
        return self.__capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, capacidade_maxima: int) -> None:
        self.__capacidade_maxima = capacidade_maxima

    @property
    def cidades(self) -> list:
        return self.__cidades

    @cidades.setter
    def cidades(self, cidades: list) -> None:
        self.__cidades = cidades

    @staticmethod
    def buscar():
        dados_restaurante = RestauranteDAO.buscar()
        if dados_restaurante is None:
            return None

        return dados_restaurante[0]
