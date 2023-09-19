from modulos.restaurante.RestauranteDAO import RestauranteDAO


class Restaurante(RestauranteDAO):
    def __init__(self, capacidade_maxima: int, id: int = None) -> None:
        super().__init__()
        if id is not None:
            self.__id = id

        self.__capacidade_maxima = capacidade_maxima

    @property
    def capacidade_maxima(self) -> int:
        return self.__capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, capacidade_maxima: int) -> None:
        self.__capacidade_maxima = capacidade_maxima

    @staticmethod
    def buscar() -> list:
        return RestauranteDAO.buscar()
