import PySimpleGUI as sg


class TelaUsuario:
    def __init__(self):
        self.__window = None

    def cadastro_senhas(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Cadastro de Senhas")],
            [sg.Text("Senha gerente", size=(15, 1)),
             sg.InputText(key='input_senha_gerente')],
            [sg.Text("Senha funcionário", size=(15, 1)),
             sg.InputText(key='input_senha_funcionario')],
            [sg.Button('Voltar'), sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('GoChef').layout(layout)

        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED or event == 'Voltar':
                return self.fechar_tela()
            if event == 'Confirmar':
                self.fechar_tela()
                return values

    def login(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Realize seu Login")],
            [sg.Radio('Gerente', 'tipo_usuario', default=True, key='gerente'),
             sg.Radio('Funcionário', 'tipo_usuario', key='funcionario')],
            [sg.Text("Senha", size=(15, 1)), sg.InputText(key='input_senha')],
            [sg.Button('Voltar'), sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('GoChef').layout(layout)

        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED or event == 'Voltar':
                return self.fechar_tela()
            if event == 'Confirmar':
                self.fechar_tela()
                return values

    def fechar_tela(self):
        self.__window.Close()

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem)
