import PySimpleGUI as sg


class TelaRestaurante:
    def __init__(self) -> None:
        sg.ChangeLookAndFeel('Material2')
        self.__window = None

    def mostra_mensagem_erro(self, mensagem: str) -> None:
        sg.popup_error(mensagem)

    def mostra_opcoes(self, nome_tela: str):
        layout = [
            [sg.Text('Tela Inicial')],
            [sg.Text('Capacidade máxima de pessoas', size=(15, 1)),
             sg.InputText(key='capacidade_maxima')],
            [sg.Text('Cidade permitidas', size=(15, 1)),
             sg.InputText(key='cidade', do_not_clear=False),
             sg.Button('Adicionar cidade')],
            [sg.Column([], key='cidades_section')],
            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window(nome_tela).Layout(layout)
        botao, valores = self.abre()
        cidades = []
        while True:
            if botao == 'Adicionar cidade':
                cidade_adicionada = valores['cidade']

                if len(cidade_adicionada) == 0:
                    self.mostra_mensagem_erro(
                        'Insira um nome correto para a cidade!')
                    botao, valores = self.abre()
                    continue

                if cidade_adicionada.isdecimal():  # TODO REGEX VERIFICADORA
                    self.mostra_mensagem_erro(
                        'O nome da cidade não deve ser composta por dígitos')
                    botao, valores = self.abre()
                    continue

                cidades.append(cidade_adicionada)
                self.__window.extend_layout(
                    self.__window['cidades_section'], [[sg.Text(f'- {cidade_adicionada}')]])
                self.__window.refresh()
                botao, valores = self.abre()
                continue

            if botao == 'Confirmar':
                if not valores['capacidade_maxima'].isdigit():
                    self.mostra_mensagem_erro(
                        'A capacidade máxima do restaurante deve ser um número!')
                    botao, valores = self.abre()
                    continue

                if len(cidades) == 0:
                    self.mostra_mensagem_erro(
                        'Cadastre pelo menos uma cidade!')
                    botao, valores = self.abre()
                    continue

                return {
                    'capacidade_maxima': valores['capacidade_maxima'],
                    'cidades': cidades,
                }

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
