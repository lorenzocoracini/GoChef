import PySimpleGUI as sg


class TelaRestaurante:
    def __init__(self) -> None:
        sg.ChangeLookAndFeel('Material2')
        self.__window = None
        self.__layout = [
            [sg.Text('Tela Inicial')],
            [sg.Text('Capacidade máxima de pessoas', size=(15, 1)),
             sg.InputText(key='capacidade_maxima')],
            [sg.Text('Cidade permitidas', size=(15, 1)),
             sg.InputText(key='cidade', do_not_clear=False),
             sg.Button('Adicionar cidade')],
            [sg.Button('Confirmar')]
        ]

    def pega_dados(self):
        self.__window = sg.Window('Tela Inicial').layout(self.__layout)

    def executa(self):
        self.pega_dados()
        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'Adicionar cidade':
                pass
                cidade = values['cidade']
                self.__layout.insert(
                    3, [sg.Text(f'- {cidade}', size=(15, 1)), sg.Button('Remover Cidade')])
                print(self.__layout)
                self.pega_dados()
            elif event == 'Confirmar':
                print(event, values)
                # senha_digitada = values['input_senha']
                # tipo_usuario = 'gerente' if values['gerente'] else 'funcionario'

                # if self.validacao(senha_digitada, tipo_usuario):
                # print(tipo_usuario)
                # return tipo_usuario
                # else:
                # sg.popup('Tipo de usuário ou senha incorretos')


if __name__ == '__main__':
    TelaRestaurante().executa()
