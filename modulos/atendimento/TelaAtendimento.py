import PySimpleGUI as sg


class TelaAtendimento:
    def __init__(self):
        sg.ChangeLookAndFeel('Material2')
        self.__window = None

    def detalhes_atendimento(self, pedidos: list = []):
        lista_de_pedidos = []
        for (index, pedido) in enumerate(pedidos):
            lista_de_pedidos.append(
                [sg.Text(f'- Pedido {index + 1}'),
                 sg.Button('Excluir', key=f"excluir {pedido['id']}")
                 ])

        layout = [
            [sg.Text("Detalhes da Mesa")],
            [sg.Column(lista_de_pedidos, key='pedidos') if len(lista_de_pedidos) > 0 else sg.Text(
                "Não há pedidos cadastrados")],
            [sg.Button('Voltar'), sg.Button('Adicionar pedido'), sg.Button('Encerrar')]
        ]

        self.__window = sg.Window('GoChef').layout(layout)

        while True:
            event, values = self.__window.read()
            if event == sg.WIN_CLOSED:
                exit(0)

            if event == 'Voltar':
                self.fechar_tela()
                return {'voltar': True}

            if event == 'Adicionar pedido':
                self.fechar_tela()
                return {'adicionar_pedido': True}

            if event == 'Encerrar':
                self.fechar_tela()
                self.mostra_mensagem("TODO: Implementar encerramento do atendimento")
                return {'encerrar': True}

            if event.startswith('excluir'):
                pedido_id = event.split().pop()
                self.fechar_tela()
                return {'excluir': pedido_id}

            else:
                self.fechar_tela()

    def fechar_tela(self):
        self.__window.Close()

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem)
