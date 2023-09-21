import bcrypt

from erros.ErroEntradaVazia import ErroEntradaVazia
from erros.ErroNaoEncontrado import ErroNaoEncontrado
from modulos.usuario.EntidadeUsuario import Usuario
from modulos.usuario.TelaUsuario import TelaUsuario

class ControladorUsuario:
  def __init__(self):
    self.__usuarios = []
    self.__tela = TelaUsuario()
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
    
  def __salvar_senha(self, gerente: bool, senha: str):
     hash_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode()
     [usuario, index] = self.buscar_por_papel(gerente)
     self.editar(usuario.id, {"senha": hash_senha})

  def __checar_senha(self, gerente: bool, senha_digitada: str) -> bool:
    [usuario, index] = self.buscar_por_papel(gerente)
    senha_correta = usuario.senha.encode('utf-8')

    return bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_correta)
    
    
  def cadastrar_senha(self):
    usuarios = Usuario.buscar();
    if usuarios[0]["senha"] != '123': return
    dados = self.__tela.cadastro_senhas()

    self.__salvar_senha(True, dados['input_senha_gerente'])
    self.__salvar_senha(False, dados['input_senha_funcionario'])

  def login(self):
    dados = self.__tela.login()

    gerente = dados["gerente"]
    
    resultado = self.__checar_senha(gerente, dados['input_senha'])

    if resultado:
      return gerente
    else:
      self.__tela.mostra_mensagem('Tipo de usuário ou senha incorretos')
      return self.__tela.cadastro_senhas()
    
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
  
  def buscar_por_papel(self, gerente: bool) -> (Usuario, int):
    # Recebe um booleano indicando se é para buscar pelo gerente ou funcionario,
    # busca ele na lista e devolve o objeto e o indice
    if not len(self.colecao):
      raise ErroEntradaVazia
    try:
      index = [x.gerente for x in self.colecao].index(gerente)
    except ValueError:
      raise ErroNaoEncontrado
    objeto = self.colecao[index]
    return (objeto, index)

  def buscar_por_id(self, id: int):
    if not len(self.colecao):
      raise ErroEntradaVazia
    try:
      index = [x.id for x in self.colecao].index(id)
    except ValueError:
      raise ErroNaoEncontrado
    objeto = self.colecao[index]
    return (objeto, index)