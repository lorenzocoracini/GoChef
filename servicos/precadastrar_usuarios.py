from modulos.usuario.EntidadeUsuario import Usuario
from modulos.usuario.ControladorUsuario import ControladorUsuario


def criar_usuarios(controlador: ControladorUsuario):
    controlador.cadastrar({"gerente": True, "senha": "123"})
    controlador.cadastrar({"gerente": False, "senha": "123"})

def precadastrar_usuarios(controlador: ControladorUsuario):
  try:
    usuarios = Usuario.buscar()
  except: 
    criar_usuarios(controlador)
    return
    
  if len(usuarios) == 0:
    criar_usuarios(controlador)