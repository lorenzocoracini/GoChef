from modulos.restaurante.RestauranteDAO import RestauranteDAO


class Restaurante(RestauranteDAO):
    def __init__(self, capacidade_maxima: int, cidades: list, id=None) -> None:
        super().__init__()
        if id is not None:
            self.__id = id
        self.__capacidade_maxima = capacidade_maxima
        # self.__cidades = [Cidade(nome_cidade) for nome_cidade in cidades]

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
