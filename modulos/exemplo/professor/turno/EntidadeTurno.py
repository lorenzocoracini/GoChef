import random
from erros.ErroEntradaVazia import ErroEntradaVazia
from modulos.exemplo.professor.turno.TurnoDAO import TurnoDAO


class Turno(TurnoDAO):

    def __init__(self, dia_semana: str, periodo: str, carga_horaria: int, professor: int, id=random.randint(1000, 9999)) -> None:
        super().__init__()
        self.__id = id
        self.__dia_semana = dia_semana
        self.__periodo = periodo
        self.__carga_horaria = carga_horaria
        self.__professor = professor

    @property
    def identificador(self):
        return self.__id

    @property
    def dia_semana(self):
        return self.__dia_semana

    @dia_semana.setter
    def dia_semana(self, dia_semana):
        self.__dia_semana = dia_semana

    @property
    def periodo(self):
        return self.__periodo

    @periodo.setter
    def periodo(self, periodo):
        self.__periodo = periodo

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    @staticmethod
    def buscar() -> list:
        return TurnoDAO.buscar()
