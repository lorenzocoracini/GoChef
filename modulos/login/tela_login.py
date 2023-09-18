import PySimpleGUI as sg
import bcrypt


class TelaLogin:

    def __init__(self):
        self.__window = None

    def pega_dados(self):
        sg.ChangeLookAndFeel('Material2')
        layout = [
            [sg.Text("Realize seu Login")],
            [sg.Radio('Gerente', 'tipo_usuario', default=True, key='gerente'),
             sg.Radio('Funcionário', 'tipo_usuario', key='funcionario')],
            [sg.Text("Senha", size=(15, 1)), sg.InputText(key='input_senha')],
            [sg.Button('Voltar'), sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('GoChef').layout(layout)

    def validacao(self, senha_digitada, tipo_usuario):
        #refatorar pra buscar as senhas cadastradas pelo gerente
        senha_gerente = "123"
        senha_funcionario = "321"

        if tipo_usuario == 'gerente':
            senha_correta = bcrypt.hashpw(senha_gerente.encode('utf-8'), bcrypt.gensalt())
        elif tipo_usuario == 'funcionario':
            senha_correta = bcrypt.hashpw(senha_funcionario.encode('utf-8'), bcrypt.gensalt())

        return bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_correta)

    def executa(self):
        self.pega_dados()
        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED or event == 'Voltar':
                break
            if event == 'Confirmar':
                senha_digitada = values['input_senha']
                tipo_usuario = 'gerente' if values['gerente'] else 'funcionario'

                if self.validacao(senha_digitada, tipo_usuario):
                    print(tipo_usuario)
                    return tipo_usuario
                else:
                    sg.popup('Tipo de usuário ou senha incorretos')


if __name__ == "__main__":
    TelaLogin().executa()
