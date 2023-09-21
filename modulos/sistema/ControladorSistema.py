from modulos.usuario.ControladorUsuario import ControladorUsuario
from modulos.usuario.EntidadeUsuario import Usuario
from modulos.restaurante.ControladorRestaurante import ControladorRestaurante


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario()
        self.__controlador_restaurante = ControladorRestaurante()

    def __criar_usuarios(self):
        try:
            usuarios = Usuario.buscar()
        except:
            self.__controlador_usuario.cadastrar(
                {"gerente": True, "senha": "123"})
            self.__controlador_usuario.cadastrar(
                {"gerente": False, "senha": "123"})
            return

        if len(usuarios) == 0:
            self.__controlador_usuario.cadastrar(
                {"gerente": True, "senha": "123"})
            self.__controlador_usuario.cadastrar(
                {"gerente": False, "senha": "123"})

    def inicializa_sistema(self):
        self.__criar_usuarios()
        self.__controlador_restaurante.cadastrar_dados_iniciais()
        self.__controlador_usuario.cadastrar_senha()
        eh_gerente = self.__controlador_usuario.login()

        print(eh_gerente)
