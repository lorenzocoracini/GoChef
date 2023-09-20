import random
from modulos.restaurante.RestauranteDAO import RestauranteDAO


class Restaurante(RestauranteDAO):
    def __init__(self, capacidade_maxima: int, id: int = random.randint(1000, 9999)) -> None:
        super().__init__()
        self.__id = id
        self.__capacidade_maxima = capacidade_maxima

    @property
    def identificador(self) -> int:
        return self.__id

    @property
    def capacidade_maxima(self) -> int:
        return self.__capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, capacidade_maxima: int) -> None:
        self.__capacidade_maxima = capacidade_maxima

    @staticmethod
    def buscar():
        dados_restaurante = RestauranteDAO.buscar()
        if dados_restaurante is None:
            return None

        return dados_restaurante[0]
