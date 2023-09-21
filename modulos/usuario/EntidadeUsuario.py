from modulos.usuario.UsuarioDAO import UsuarioDAO


class Usuario(UsuarioDAO):
    def __init__(self, gerente: bool, senha: str, id = None) -> None:
        UsuarioDAO.__init__(self)
        if id: 
            self.__id = id
        self.__gerente = gerente
        self.__senha = senha

    @property
    def id(self):
        return self.__id

    @property
    def gerente(self):
        return self.__gerente
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @staticmethod
    def buscar() -> list:
        return UsuarioDAO.buscar()
