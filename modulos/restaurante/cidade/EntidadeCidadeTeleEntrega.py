from modulos.restaurante.cidade.CidadeTeleEntregaDAO import CidadeTeleEntregaDAO


class CidadeTeleEntrega(CidadeTeleEntregaDAO):
    def __init__(self, nome: str) -> None:
        super().__init__()
        self.__nome = nome

    @property
    def identificador(self) -> str:
        return self.__nome

    @property
    def nome(self) -> str:
        return self.__nome

    @staticmethod
    def buscar():
        dados_cidades = CidadeTeleEntregaDAO.buscar()
        if dados_cidades is None:
            return None

        return dados_cidades
