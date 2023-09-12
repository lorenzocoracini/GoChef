import random
from modulos.exemplo.EntidadePessoa import Pessoa
from modulos.exemplo.professor.ProfessorDAO import ProfessorDAO


class Professor(Pessoa, ProfessorDAO):

    def __init__(self, nome: str, cpf: str, peso: int, altura: float, salario: float, id=random.randint(1000, 9999)) -> None:
        Pessoa.__init__(self, nome, cpf, peso, altura, id)
        ProfessorDAO.__init__(self)
        self.__salario = salario
        self.__turnos_ = None

    @property
    def salario(self):
        return self.__salario

    @property
    def turnos(self):
        return self.__turnos_

    @turnos.setter
    def turnos(self, turnos: list):
        self.__turnos_ = turnos

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @staticmethod
    def buscar() -> list:
        return ProfessorDAO.buscar()
