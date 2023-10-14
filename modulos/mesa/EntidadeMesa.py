from modulos.mesa.MesaDAO import MesaDAO


class Mesa(MesaDAO):
    def __init__(self, numero_lugares: int, numero_mesa: str, id = None) -> None:
        MesaDAO.__init__(self)
        if id: 
            self.__id = id
        self.__numero_lugares = numero_lugares
        self.__numero_mesa = numero_mesa
        self.__atendimentos = None

    @property
    def id(self):
        return self.__id

    @property
    def numero_lugares(self):
        return self.__numero_lugares

    @numero_lugares.setter
    def numero_lugares(self, numero_lugares):
        self.__numero_lugares = numero_lugares
    
    @property
    def numero_mesa(self):
        return self.__numero_mesa
    
    @numero_mesa.setter
    def numero_mesa(self, numero_mesa):
        self.__numero_mesa = numero_mesa

    @property
    def atendimentos(self) -> list:
        return self.__atendimentos

    @atendimentos.setter
    def atendimentos(self, atendimentos: list) -> None:
        self.__atendimentos = atendimentos

    @staticmethod
    def buscar() -> list:
        return MesaDAO.buscar()
