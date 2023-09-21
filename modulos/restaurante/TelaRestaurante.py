import PySimpleGUI as sg
import re


class TelaRestaurante:
    def __init__(self) -> None:
        sg.ChangeLookAndFeel('Material2')
        self.__window = None

    def mostra_mensagem_erro(self, mensagem: str) -> None:
        sg.popup_error(mensagem)

    def valida_string(self, valor: str, min_len=None, max_len=None):
        if valor.strip() == '':
            raise ValueError('Entrada inválida. O valor não pode ser vazio.')
        if re.search('\d', valor):
            raise ValueError(
                'Entrada inválida. O valor não deve conter dígitos.')
        if min_len and len(valor) < min_len:
            raise ValueError(
                f'A entrada deve ter no mínimo {min_len} caracteres!')
        if max_len and len(valor) > max_len:
            raise ValueError(
                f'A entrada deve ter no máximo {max_len} caracteres!')

    def valida_inteiro(self, valor: str):
        try:
            return int(valor)
        except:
            raise ValueError('Por favor, insira um número inteiro.')

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
            try:
                print('BOTAO', botao)
                if botao == 'Adicionar cidade':
                    cidade_adicionada = valores['cidade']
                    self.valida_string(cidade_adicionada)
                    cidades.append(cidade_adicionada)
                    self.__window.extend_layout(
                        self.__window['cidades_section'], [[sg.Text(f'- {cidade_adicionada}', key=f'cidade_{cidade_adicionada}'), sg.Button('Remover cidade', key=cidade_adicionada)]])
                    self.__window.refresh()
                    botao, valores = self.abre()
                    continue

                if botao in cidades:

                    cidades.remove(botao)
                    botao_remove_cidade = self.__window[f'cidade_{botao}']

                    elemento_cidade = self.__window[botao]

                    botao_remove_cidade.hide_row()
                    elemento_cidade.hide_row()

                    self.__window.refresh()
                    botao, valores = self.abre()
                    continue

                if botao == 'Confirmar':
                    if len(cidades) == 0:
                        raise ValueError(
                            'Por favor, insira pelo menos uma cidade.')

                    capacidade_maxima = self.valida_inteiro(
                        valores['capacidade_maxima'])

                    return {
                        'capacidade_maxima': capacidade_maxima,
                        'cidades': cidades,
                    }
            except Exception as err:
                self.mostra_mensagem_erro(err)
                print(err)
                botao, valores = self.abre()

    def abre(self):
        return self.__window.Read()

    def fecha(self):
        self.__window.Close()
