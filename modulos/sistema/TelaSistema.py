import PySimpleGUI as sg


class TelaSistema:
    def __init__(self) -> None:
        sg.ChangeLookAndFeel('Material2')
        self.__window = None

    def abre(self):
        return self.__window.Read()

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem_erro(self, mensagem: str) -> None:
        sg.popup_error(mensagem)

    def mostra_opcoes_funcionario(self):
        layout = [
            [sg.Text('Menu Principal GoChef')],
            [sg.Text('Selecione uma opção')],
            [sg.Radio('Controle das Mesas', 'RD1', key='1')],
            [sg.Button('Encerrar'), sg.Button('Confirmar')],
        ]

        self.__window = sg.Window('Go Chef').Layout(layout)
        botao, valores = self.abre()
        if botao in (None, 'Encerrar'):
            self.fecha()
            return 0
        for chave in valores:
            if valores[chave]:
                self.fecha()
                return int(chave)
        self.mostra_mensagem_erro('Por favor, selecione um opção!')
        botao, valores = self.abre()

    def mostra_opcoes_gerente(self):
        layout = [
            [sg.Text('Menu Principal GoChef')],
            [sg.Text('Selecione uma opção')],
            [sg.Radio('Dados do restaurante', 'RD1', key='1')],
            [sg.Radio('Senhas do sistema', 'RD1', key='2')],
            [sg.Radio('Produtos do Restaurante', 'RD1', key='3')],
            [sg.Radio('Controle das Mesas', 'RD1', key='4')],
            [sg.Button('Encerrar'), sg.Button('Confirmar')],
        ]

        self.__window = sg.Window('Go Chef').Layout(layout)
        botao, valores = self.abre()
        while True:
            if botao in (None, 'Encerrar'):
                self.fecha()
                return 0
            for chave in valores:
                if valores[chave]:
                    self.fecha()
                    return int(chave)
            self.mostra_mensagem_erro('Por favor, selecione um opção!')
            botao, valores = self.abre()
