from servicos.precadastrar_usuarios import precadastrar_usuarios

from modulos.usuario.ControladorUsuario import ControladorUsuario

controladorUsuario = ControladorUsuario()

if __name__ == "__main__":
    precadastrar_usuarios(controladorUsuario)
