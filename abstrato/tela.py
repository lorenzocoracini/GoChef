from abc import ABC
import re
from erros import ErroNaoEncontrado
from erros.InputInvalido import InputInvalido
from erros.CPFInvalido import CPFInvalido
from erros.ErroEntradaVazia import ErroEntradaVazia
from erros.ErroRelacionamentoObrigatorio import ErroRelacionamentoObrigatorio


class Tela:
  def __init__(self, titulo, objeto, opcoes, controlador):
    ''' titulo: str '''
    self.__titulo = titulo
    '''
    objeto: [key: str]: [Nome: str, tipo: <T>, editavel: bool, f_validar(), *args]
    '''
    self.__objeto = objeto
    ''' opcoes: [key: int]: [Descricao: str, funcao()] '''
    self.__opcoes = opcoes
    ''' controlador: classe de controlador'''
    self.__controlador = controlador

  @property
  def titulo(self):
    return self.__titulo

  @property
  def objeto(self):
    return self.__objeto
  
  @property
  def opcoes(self):
    return self.__opcoes

  @property
  def controlador(self):
    return self.__controlador

  def voltar(self):
    return

  def inserir_inteiro(self, message, opcoes: list = None) -> int:
    if opcoes: print(f"Insira um valor numérico inteiro dentre as seguintes opções: {' '.join([str(x) for x in opcoes])}")
    while True:
      try:
        i = int(input(message))
        if opcoes:
          if i not in opcoes:
            raise ValueError

      except ValueError:
        if not opcoes: 
          print('Insira um valor numérico inteiro.')
        elif opcoes: 
          print(f"Insira um valor numérico inteiro dentre as seguintes opções: {' '.join([str(x) for x in opcoes])}")
      else:
        return int(i)

  def inserir_float(self, message, opcoes: list = None) -> int:
    if opcoes: print(f"Insira um valor numérico decimal dentre as seguintes opções: {' '.join([str(x) for x in opcoes])}")
    while True:
      try:
        i = float(input(message))
        if opcoes:
          if i not in opcoes:
            raise ValueError

      except ValueError:
        if not opcoes: 
          print('Insira um valor numérico valido.')
        elif opcoes: 
          print(f"Insira um valor numérico dentre as seguintes opções: {' '.join([str(x) for x in opcoes])}")
      else:
        return float(i)
   
  def inserir_string(self, mensagem = 'Insira uma string: ', min_len = None, max_len = None):
    while True:
      try:
        entrada = input(mensagem)
        if entrada.strip() == '':
          raise ErroEntradaVazia
        if min_len and len(entrada) < min_len:
          raise InputInvalido
        if max_len and len(entrada) > max_len:
          raise InputInvalido
      
      except (InputInvalido, ErroEntradaVazia) as e:
        print(e)
        texto = '\n'+mensagem    
        if min_len: texto += f'\n- No mínimo {min_len} caracteres'
        if max_len: texto += f'\n- No máximo {max_len} caracteres'
        print(texto)
      else:
        return entrada

  def inserir_enum(self, mensagem, opcoes: dict):
    for opcao, tipo in opcoes.items():
      print(f'{opcao} - {tipo}')
    entrada = self.inserir_inteiro(mensagem, opcoes)
    return opcoes[entrada]

  def selecionar_estrangeiro(self, mensagem, controlador_estrangeiro, entidade_estrangeira):
    try:
      id_estrangeiros = self.listar(controlador_estrangeiro, entidade_estrangeira)
      chave_estrangeira = self.inserir_inteiro(mensagem, id_estrangeiros)
    except ErroEntradaVazia:
      error = f'Não há {entidade_estrangeira} cadastrados ainda. Faça o cadastro de {entidade_estrangeira} antes de prosseguir.'
      raise ErroRelacionamentoObrigatorio(error)
    return chave_estrangeira

  def inserir_cpf(self, mensagem: str):
    while True:
      mascara_cpf = re.compile('\d{3}\.\d{3}\.\d{3}\-\d{2}')
      cpf = self.inserir_string(mensagem)

      try:
        if mascara_cpf.search(cpf):
          return cpf
        else:
          raise CPFInvalido
      except CPFInvalido as e:
        print(e)

  def mostrar_opcoes(self):
    escolha = 0
    print(f'\n--- {self.titulo} ---')
    for opcao, data in self.opcoes.items():
      print(f'{opcao} - {data[0]}')
    escolha = self.inserir_inteiro('\nDigite a opção escolhida: ', list(self.opcoes.keys()))
    
    self.opcoes[escolha][1]()

  def pegar_dados(self, dados = None) -> dict:
    if not dados: dados = self.objeto
    objeto = {}
    for atributo, data in dados.items():
      if(data[2]): # se for editável
        if(data[4]): # se houver params, chama a função com os parâmetros
          valor = data[3](*data[4])
        else:
          valor = data[3]()
        objeto[atributo] = valor
    
    return objeto

  def cadastrar(self):
    try:
      dados = self.pegar_dados()
    except ErroRelacionamentoObrigatorio as e:
      print(e)
      return
    try:
      self.__controlador.cadastrar(dados)
    except:
      print(f'Ocorreu um problema ao cadastrar o objeto. Tente novamente.')
      raise
    else:
      print('Objeto cadastrado com sucesso.')

  def editar(self):
    try:
      id_registros = self.listar()
      identificador = self.inserir_inteiro('Digite o id que deseja editar: ', id_registros)
      dados = self.pegar_dados()
      self.__controlador.editar(identificador, dados)
    except ErroEntradaVazia:
      print(f'Não há {self.titulo} cadastrados ainda.')
    except ErroNaoEncontrado:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
    except:
      print(f'Ocorreu um problema ao editar o objeto. Tente novamente.')
    else:
      print(f'Editado com sucesso.')

  def listar(self, tela = 1, titulo = 1) -> list:
    if tela == 1: 
      objeto = self.objeto
      colecao = self.__controlador.colecao
    else:
      objeto = tela.objeto
      colecao = tela.controlador.colecao
    if titulo == 1: titulo = self.titulo
    identificadores = []
    if len(colecao):
      print(f'\n-- Lista de {titulo} --')
      for item in colecao:
        print()
        identificadores.append(item.identificador)
        print(f'ID: {item.identificador}')
        for atributo in [atributo for atributo in item.atributos if not atributo == 'id']:
          print(f'{objeto[atributo][0]}: {getattr(item, atributo)}')
      print()
      return identificadores
    else:
      print(f'Não há {self.titulo} cadastrados ainda.')
      return

  def deletar(self):
    try:
      id_registros = self.listar()
      identificador = self.inserir_inteiro('Digite o id que deseja deletar: ', id_registros)
      self.__controlador.deletar(identificador)
    except ErroRelacionamentoObrigatorio:
      print(f'Não há {self.titulo} cadastrados ainda.')
      return
    except ErroNaoEncontrado:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
      return
    except:
      print(f'Ocorreu um problema ao deletar o objeto. Tente novamente.')
      return
    else:
      print(f'Deletado com sucesso.')
