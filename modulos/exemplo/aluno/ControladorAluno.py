from datetime import date

from erros.ErroEntradaVazia import ErroEntradaVazia
from erros.ErroNaoEncontrado import ErroNaoEncontrado
from modulos.exemplo.aluno.EntidadeAluno import Aluno

class ControladorAluno:
  def __init__(self):
    self.__alunos = []
    try:
      self.carregar_dados()
    except ErroEntradaVazia:
      pass

  @property
  def colecao(self):
    return self.__alunos

  @colecao.setter
  def colecao(self, colecao):
    self.__alunos = colecao

  def cadastrar(self, dados: dict):
    try:
      dados['data_matricula'] = date.today()
      novo_aluno = Aluno(**dados)
      novo_aluno.guardar()
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

  def deletar(self, id):
    try:
      [objeto, _] = self.buscar_por_id(id)
      objeto.remover()
      self.carregar_dados()
    except ErroNaoEncontrado:
      raise ErroNaoEncontrado
    except:
      raise ValueError

  def carregar_dados(self):
    # Busca todos os cadastros e popula a listagem
    result = Aluno.buscar()
    self.colecao = []
    for dados in result:
      objeto = Aluno(**dados)
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