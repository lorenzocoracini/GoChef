import PySimpleGUI as sg


class TelaPedido:
    def __init__(self, lista_de_produtos):
        sg.ChangeLookAndFeel('Material2')
        self.__window = None
        self.lista_de_produtos = lista_de_produtos
        self.pedido = {}

    def mostrar_interface(self):
        layout = [
            [sg.Text('Selecione o produto:')],
            [sg.Listbox(self.lista_de_produtos, size=(30, 6), key='produto_list')],
            [sg.Text('Quantidade:'), sg.InputText(key='quantidade')],
            [sg.Button('Adicionar ao Pedido'), sg.Button('Concluir Pedido')],
            [sg.Text('Itens no Pedido:')],
            [sg.Multiline('', size=(40, 10), key='pedido_text', autoscroll=True)],
        ]

        self.__window = sg.Window('Criação de Pedido', layout)

        while True:
            event, values = self.__window.read()

            if event in (sg.WIN_CLOSED, 'Concluir Pedido'):
                break
            elif event == 'Adicionar ao Pedido':
                produto_selecionado = values['produto_list'][0]
                quantidade = values['quantidade']

                if produto_selecionado and quantidade:
                    quantidade = int(quantidade)
                    if produto_selecionado in self.pedido:
                        self.pedido[produto_selecionado] += quantidade
                    else:
                        self.pedido[produto_selecionado] = quantidade
                    self.atualizar_resumo_do_pedido(self.__window)

        self.__window.close()

    def atualizar_resumo_do_pedido(self, window):
        pedido_text = '\n'.join([f'{produto}: {quantidade}' for produto, quantidade in self.pedido.items()])
        window['pedido_text'].update(pedido_text)

    def obter_pedido(self):
        return self.pedido


if __name__ == '__main__':
    lista_de_produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4']
    pedido = TelaPedido(lista_de_produtos)
    pedido.mostrar_interface()
    pedido_final = pedido.obter_pedido()
    print('Pedido Final:')
    for produto, quantidade in pedido_final.items():
        print(f'{produto}: {quantidade}')
