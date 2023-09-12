import random
from modulos.exemplo.EntidadePessoa import Pessoa
from modulos.exemplo.aluno.AlunoDAO import AlunoDAO


class Aluno(Pessoa, AlunoDAO):

    def __init__(self, nome: str, cpf: str, peso: int, altura: float, data_matricula: str, id=None) -> None:
        if not id:
            id = random.randint(1000, 9999)
        Pessoa.__init__(self, nome, cpf, peso, altura, id)
        AlunoDAO.__init__(self)
        self.__data_matricula = data_matricula

    @property
    def data_matricula(self):
        return self.__data_matricula

    @data_matricula.setter
    def data_matricula(self, data_matricula):
        self.__data_matricula = data_matricula

    @staticmethod
    def buscar() -> list:
        return AlunoDAO.buscar()
