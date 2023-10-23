import PySimpleGUI as sg


class TelaMesa:
    def __init__(self):
        sg.ChangeLookAndFeel('Material2')
        self.__window = None

    def lista_mesas(self, mesas_atendidas: list, mesas_nao_atendidas: list, eh_gerente: bool):
        print("mesas_atendidas ---- ", mesas_atendidas)
        print("mesas_nao_atendidas ---- ", mesas_nao_atendidas)
        lista_de_mesas = []
        for mesa in mesas_nao_atendidas:
            lista_de_mesas.append(
                [sg.Text(f'- Mesa {mesa.numero_mesa}'),
                 sg.Button('Iniciar atendimento', key=f"atendimento {mesa.id}"),
                 sg.Button('Editar', key=f"editar {mesa.id}", visible=eh_gerente),
                 sg.Button('Excluir', key=f"excluir {mesa.id}", visible=eh_gerente)
                 ])
        for mesa in mesas_atendidas:
            lista_de_mesas.append(
                [sg.Text(f'- Mesa {mesa.numero_mesa}'),
                 sg.Button('Detalhes', key=f"atendimento {mesa.id}"),
                 sg.Button('Editar', key=f"editar {mesa.id}", visible=eh_gerente),
                 sg.Button('Excluir', key=f"excluir {mesa.id}", visible=eh_gerente)
                 ])

        layout = [
            [sg.Text("Mesas")],
            [sg.Column(lista_de_mesas, key='mesas') if len(lista_de_mesas) > 0 else sg.Text(
                "Não há mesas cadastradas")],
            [sg.Button('Voltar'), sg.Button('Adicionar', visible=eh_gerente)]
        ]

        self.__window = sg.Window('GoChef').layout(layout)

        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED:
                exit(0)

            if event == 'Voltar':
                self.fechar_tela()
                return {'voltar': True}

            if event == 'Adicionar':
                self.fechar_tela()
                return {'adicionar': True}

            if event.startswith('atendimento'):
                mesa = event.split().pop()
                self.fechar_tela()
                return {'atendimento': mesa}

            if event.startswith('editar'):
                mesa = event.split().pop()
                self.fechar_tela()
                return {'editar': mesa}

            if event.startswith('excluir'):
                mesa = event.split().pop()
                self.fechar_tela()
                return {'excluir': mesa}


            else:
                self.fechar_tela()

    def mostra_formulario(self, numero_mesa_cadastrado=None, numero_lugares_cadastrado=None):
        layout = [
            [sg.Text("Cadastro de Mesa")],
            [sg.Text("Numero da mesa", size=(15, 1)),
             sg.InputText(key='input_numero_mesa', default_text=numero_mesa_cadastrado)],
            [sg.Text("Numero de lugares", size=(15, 1)),
             sg.InputText(key='input_numero_lugares', default_text=numero_lugares_cadastrado)],
            [sg.Button('Voltar'), sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('GoChef').layout(layout)

        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED:
                exit(0)

            if event == 'Confirmar':
                campos_validados = self.__validar_campos_mesa(values['input_numero_mesa'],
                                                              values['input_numero_lugares'])
                if (campos_validados):
                    self.fechar_tela()
                    return campos_validados

            if event == 'Voltar':
                self.fechar_tela()
                return {'voltar': True}

            else:
                self.fechar_tela()

    def __validar_campos_mesa(self, numero_mesa: str, numero_lugares: str):
        if not numero_mesa or not numero_lugares:
            self.mostra_mensagem('Por favor, digite todos os campos!')
        try:
            numero_mesa = int(numero_mesa)
            if numero_mesa < 0:
                raise ValueError
        except ValueError:
            self.mostra_mensagem('O número da mesa deve ser um número inteiro positivo')
            return False

        try:
            numero_lugares = int(numero_lugares)
            if numero_lugares < 1:
                raise ValueError
        except ValueError:
            self.mostra_mensagem('O número da mesa deve ser um número inteiro positivo maior que 1')
            return False

        return {'numero_mesa': numero_mesa, 'numero_lugares': numero_lugares}

    def confirma_exclusao_mesa(self, numero_mesa: int):
        mensagem_confirmacao = f'''
                Você tem certeza que deseja excluir a Mesa {numero_mesa}?
            '''
        layout = [
            [sg.Text(mensagem_confirmacao)],
            [sg.Button('Não'), sg.Button('Sim')]
        ]

        self.__window = sg.Window('Remover Mesa').Layout(layout)
        botao, valores = self.__window.read()

        if not botao:
            exit(0)

        self.fechar_tela()
        return botao == 'Sim'

    def fechar_tela(self):
        self.__window.Close()

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem)
