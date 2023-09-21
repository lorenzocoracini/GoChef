from modulos.usuario.ControladorUsuario import ControladorUsuario
from modulos.usuario.EntidadeUsuario import Usuario


class ControladorSistema:
  def __init__(self):
    self.__controladorUsuario = ControladorUsuario()

  def __criar_usuarios(self):
    try:
      usuarios = Usuario.buscar()
    except:
      self.__controladorUsuario.cadastrar({"gerente": True, "senha": "123"})
      self.__controladorUsuario.cadastrar({"gerente": False, "senha": "123"})
      return
      
    if len(usuarios) == 0:
      self.__controladorUsuario.cadastrar({"gerente": True, "senha": "123"})
      self.__controladorUsuario.cadastrar({"gerente": False, "senha": "123"})


  def inicializa_sistema(self):
    self.__criar_usuarios()
    self.__controladorUsuario.cadastrar_senha()
    eh_gerente = self.__controladorUsuario.login()

    print(eh_gerente)


  