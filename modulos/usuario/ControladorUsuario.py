from datetime import date

from erros.ErroEntradaVazia import ErroEntradaVazia
from erros.ErroNaoEncontrado import ErroNaoEncontrado
from modulos.usuario.EntidadeUsuario import Usuario

class ControladorUsuario:
  def __init__(self):
    self.__usuarios = []
    try:
      self.carregar_dados()
    except ErroEntradaVazia:
      pass

  @property
  def colecao(self):
    return self.__usuarios

  @colecao.setter
  def colecao(self, colecao):
    self.__usuarios = colecao

  def cadastrar(self, dados: dict):
    try:
      novo_usuario = Usuario(**dados)
      novo_usuario.guardar()
      self.carregar_dados()
    except:
      raise ValueError

  def editar(self, id, dados: dict):
    try:
      [objeto, _] = self.buscar_por_id(id)
      for chave, valor in dados.items():
        setattr(objeto, chave, valor)
      objeto.atualizar()
    except (ErroEntradaVazia, ErroNaoEncontrado):
      raise
    except:
      raise ValueError

  def carregar_dados(self):
    # Busca todos os cadastros e popula a listagem
    result = Usuario.buscar()
    self.colecao = []
    for dados in result:
      objeto = Usuario(**dados)
      self.colecao.append(objeto)

  def buscar_por_id(self, id):
    # Recebe um id, busca ele na lista e devolve o objeto e o indice
    if not len(self.colecao):
      raise ErroEntradaVazia
    try:
      index = [x.identificador for x in self.colecao].index(id)
    except ValueError:
      raise ErroNaoEncontrado
    objeto = self.colecao[index]
    return (objeto, index)