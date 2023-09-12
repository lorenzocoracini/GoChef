import random
from erros.ErroEntradaVazia import ErroEntradaVazia


class Pessoa:
    def __init__(self, nome: str, cpf: str, peso: int, altura: float, id=None) -> None:
        if not id:
            id = random.randint(1000, 9999)
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__peso = peso
        self.__altura = altura

    @property
    def identificador(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura
