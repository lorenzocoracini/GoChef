from abstrato.tela import Tela
from erros import ErroEntradaVazia, ErroNaoEncontrado


class TelaProfessor(Tela):
  def __init__(self, controlador):
    titulo = 'Professores'
    objeto = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "nome": ['Nome', str, True, self.inserir_string, ['Insira o nome: ']],
      "cpf": ['CPF', str, True, self.inserir_cpf, ['Insira o CPF: ']],
      "peso": ['Peso', str, True, self.inserir_inteiro, ['Insira o peso: ']],
      "altura": ['Altura', str, True, self.inserir_float, ['Insira a altura: ']],
      "salario": ['Salário', str, True, self.inserir_float, ['Insira o salário: ']],
    }
    opcoes = {
      1: ['Cadastrar um professor', self.cadastrar],
      2: ['Editar um professor', self.editar],
      3: ['Listar professores', self.listar],
      4: ['Deletar um professor', self.deletar],
      5: ['Voltar', self.voltar]
    }
    dias_semana = {
      1: "Segunda Feira",
      2: "Terça Feira",
      3: "Quarta Feira",
      4: "Quinta Feira",
      5: "Sexta Feira",
      6: "Sábado"
    }
    periodos = {
      1: "Manhã",
      2: "Tarde",
      3: "Noite"
    }
    self.objeto_turno = {
      "id": ['Identificador', int, False, self.inserir_inteiro, None],
      "dia_semana": ['Dia da semana', str, True, self.inserir_enum, ['Insira o dia da semana: ', dias_semana]],
      "periodo": ['Período', str, True, self.inserir_enum, ['Insira o período: ', periodos]],
      "carga_horaria": ['Carga horária', str, True, self.inserir_inteiro, ['Insira a carga horária: ']],
    }
    super().__init__(titulo, objeto, opcoes, controlador)

  def listar(self,) -> list:
    identificadores = []
    if len(self.controlador.colecao):
      print(f'\n-- Lista de Professores --')
      for item in self.controlador.colecao:
        print()
        identificadores.append(item.identificador)
        print(f'ID: {item.identificador}')
        for atributo in [atributo for atributo in item.atributos if not atributo == 'id']:
          print(f'{self.objeto[atributo][0]}: {getattr(item, atributo)}')
        self.visualizar_turnos(item.identificador)
      print()
      return identificadores
    else:
      print(f'Não há {self.titulo} cadastrados ainda.')
      return
  
  def cadastrar(self):
    dados = self.pegar_dados()
    turnos = self.cadastrar_turnos()
    try:
      self.controlador.cadastrar(dados, turnos)
    except:
      print(f'Ocorreu um problema ao cadastrar o professor. Tente novamente.')
      raise
    else:
      print('Professor cadastrado com sucesso.')
  
  def editar(self):
    try:
      id_registros = self.listar()
      identificador = self.inserir_inteiro('Digite o id que deseja editar: ', id_registros)
      dados = self.pegar_dados()

      opcao = self.opcoes_edicao_turno()
      if opcao == 1:
        dados_turnos_cadastro = self.cadastrar_turnos()
        self.controlador.cadastrar_turno(identificador, dados_turnos_cadastro)
      if opcao == 2:
        dados_turnos_edicao = self.editar_turnos(identificador)
        self.controlador.editar(identificador, dados, dados_turnos_edicao)
      if opcao == 3:
        self.listar_turnos(identificador)
      if opcao == 4:
        self.deletar_turno(identificador)
      if opcao == 5:
        self.controlador.editar(identificador, dados, [])
    
    except ErroEntradaVazia:
      print(f'Não há {self.titulo} cadastrados ainda.')
    except ErroNaoEncontrado:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
    except:
      print(f'Ocorreu um problema ao editar o objeto. Tente novamente.')
    else:
      print(f'Professor editado com sucesso.')

  def opcoes_edicao_turno(self):
    print()
    print('1 - Cadastrar um novo turno')
    print('2 - Editar um turno existente')
    print('3 - Listar turnos do professor')
    print('4 - Deletar um turno')
    print('5 - Não quero editar os turnos')
    return self.inserir_inteiro('Escolha a opção: ', [1,2,3,4, 5])

  def cadastrar_turnos(self):
    print("\n-- Cadastrar turnos do professor --\n")
    turnos = []
    registrar_turnos = ''
    while registrar_turnos.lower() != 'n':
      dados_turno = self.pegar_dados(self.objeto_turno)
      turnos.append(dados_turno)

      registrar_turnos = self.inserir_string("Continuar cadastrando turnos? (digite 'n' para parar)")
      
    return turnos

  def editar_turnos(self, id_professor):
    print("\n-- Editar turnos do professor --\n")
    turnos_editados = []
    editando_turnos = ''
    while editando_turnos.lower() != 'n':
      id_turnos = self.listar_turnos(id_professor)
      identificador_turno = self.inserir_inteiro('Digite o id que deseja editar: ', id_turnos)
      dados_turno = self.pegar_dados(self.objeto_turno)
      dados_turno['id'] = identificador_turno
      dados_turno['professor'] = id_professor
      turnos_editados.append(dados_turno)

      editando_turnos = self.inserir_string("Continuar editando turnos? (digite 'n' para parar)")
    
    return turnos_editados

  def visualizar_turnos(self, id_professor):
    [professor, _] = self.controlador.buscar_por_id(id_professor)
    print('Turnos:')
    for turno in professor.turnos:
      print(f"\t{'-'*10}")
      print(f'\tDia da semana: {turno["dia_semana"]}')
      print(f'\tPeriodo: {turno["periodo"]}')
      print(f'\tCarga horária: {turno["carga_horaria"]}')

  def listar_turnos(self, id_professor):
    [professor, _] = self.controlador.buscar_por_id(id_professor)
    id_turnos = []
    print(f'\n-- Lista de Turnos --')
    for turno in professor.turnos:
      id_turnos.append(turno["id"])
      print()
      print(f'ID: {turno["id"]}')
      print(f'Dia da semana: {turno["dia_semana"]}')
      print(f'Periodo: {turno["periodo"]}')
      print(f'Carga horária: {turno["carga_horaria"]}')
    
    return id_turnos

  def deletar_turno(self, id_professor):
    try:
      id_registros = self.listar_turnos(id_professor)
      identificador = self.inserir_inteiro('Digite o id que deseja deletar: ', id_registros)
      self.controlador.deletar_turno(identificador)
    except ErroEntradaVazia:
      print(f'Não há turnos cadastrados ainda.')
      return
    except ErroNaoEncontrado:
      print(f'Nenhum objeto encontrado com id = {identificador}. Tente novamente.')
      return
    except:
      print(f'Ocorreu um problema ao deletar o objeto. Tente novamente.')
      return
    else:
      print(f'Turno deletado com sucesso.')
