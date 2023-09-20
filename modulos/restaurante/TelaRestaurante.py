import PySimpleGUI as sg


class TelaRestaurante:
    def __init__(self) -> None:
        sg.ChangeLookAndFeel('Material2')
        self.__window = None

    def mostra_opcoes(self, nome_tela: str, layout_pre_definido=None):
        layout = [
            [sg.Text('Tela Inicial')],
            [sg.Text('Capacidade máxima de pessoas', size=(15, 1)),
             sg.InputText(key='capacidade_maxima')],
            [sg.Text('Cidade permitidas', size=(15, 1)),
             sg.InputText(key='cidade', do_not_clear=False),
             sg.Button('Adicionar cidade')],
            [sg.Button('Confirmar')]
        ]
        if layout_pre_definido is not None:
            layout = layout_pre_definido

        self.__window = sg.Window(nome_tela).Layout(layout)
        while True:
            botao, valores = self.abre()
            if botao == 'Adicionar cidade':
                print('BOTÃO', botao)
                print('VALORES', valores)
                # tratar adicao de cidades
                # return
            else:
                break
        return valores

    def abre(self):
        return self.__window.Read()

    def fecha(self):
        self.__window.Close()

    # def executa(self):
    #     self.pega_dados()
    #     while True:
    #         event, values = self.__window.read()
    #         if event == sg.WIN_CLOSED:
    #             break

    #         if event == 'Adicionar cidade':
    #             pass
    #             cidade = values['cidade']
    #             self.__layout.insert(
    #                 3, [sg.Text(f'- {cidade}', size=(15, 1)), sg.Button('Remover Cidade')])
    #             print(self.__layout)
    #             self.pega_dados()
    #         elif event == 'Confirmar':
    #             print(event, values)
    #             # senha_digitada = values['input_senha']
    #             # tipo_usuario = 'gerente' if values['gerente'] else 'funcionario'

    #             # if self.validacao(senha_digitada, tipo_usuario):
    #             # print(tipo_usuario)
    #             # return tipo_usuario
    #             # else:
    #             # sg.popup('Tipo de usuário ou senha incorretos')

  # def pega_dados(self):
    #     self.__window = sg.Window('Tela Inicial').layout(self.__layout)
