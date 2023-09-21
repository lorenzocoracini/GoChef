import PySimpleGUI as sg
import re


class TelaRestaurante:
    def __init__(self) -> None:
        sg.ChangeLookAndFeel('Material2')
        self.__window = None

    def abre(self):
        return self.__window.Read()

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem_erro(self, mensagem: str) -> None:
        sg.popup_error(mensagem)

    def trata_string(self, valor: str, min_len=None, max_len=None):
        valor_tratado = ' '.join(
            [palavra[0].upper() + palavra[1:] for palavra in valor.split()])
        if not valor_tratado:
            raise ValueError('Entrada inválida. O valor não pode ser vazio.')
        if re.search('\d', valor_tratado):
            raise ValueError(
                'Entrada inválida. O valor não deve conter dígitos.')
        if min_len and len(valor_tratado) < min_len:
            raise ValueError(
                f'A entrada deve ter no mínimo {min_len} caracteres!')
        if max_len and len(valor_tratado) > max_len:
            raise ValueError(
                f'A entrada deve ter no máximo {max_len} caracteres!')

        return valor_tratado

    def valida_inteiro(self, valor: str, nome_campo=None):
        try:
            return int(valor)
        except:
            erro = 'Por favor, insira um número inteiro'
            if nome_campo:
                raise ValueError(erro + f' no campo {nome_campo}.')
            raise ValueError(erro + '.')

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
        index = 0
        while True:
            try:
                if botao == 'Adicionar cidade':
                    raw_cidade = valores['cidade']
                    cidade_adicionada = self.trata_string(raw_cidade, 3)
                    if cidade_adicionada in cidades:
                        raise ValueError('Cidade já foi adicionada')

                    cidades.append(cidade_adicionada)
                    self.__window.extend_layout(
                        self.__window['cidades_section'], [[sg.Text(f'- {cidade_adicionada}', key=f'nova_cidade {cidade_adicionada} {index}'), sg.Button('Remover cidade', key=f'remove_cidade {cidade_adicionada} {index}')]])
                    index += 1
                    self.__window.refresh()
                    botao, valores = self.abre()
                    continue

                if botao.startswith('remove_cidade'):
                    _, cidade_a_ser_removida, ind = botao.split(' ')
                    self.__window[f'nova_cidade {cidade_a_ser_removida} {ind}'].hide_row(
                    )
                    cidades.remove(cidade_a_ser_removida)
                    self.__window.refresh()
                    botao, valores = self.abre()
                    continue

                if botao == 'Confirmar':
                    if len(cidades) == 0:
                        raise ValueError(
                            'Por favor, insira pelo menos uma cidade.')

                    capacidade_maxima = self.valida_inteiro(
                        valores['capacidade_maxima'], 'capacidade máxima')

                    self.fecha()
                    return {
                        'capacidade_maxima': capacidade_maxima,
                        'cidades': cidades,
                    }
            except Exception as err:
                self.mostra_mensagem_erro(err)
                botao, valores = self.abre()
