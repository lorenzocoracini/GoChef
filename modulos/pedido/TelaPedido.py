import PySimpleGUI as sg


class TelaPedido:
    def __init__(self):
        sg.ChangeLookAndFeel('Material2')
        self.__window = None
        self.pedido = []
        self.produtos = []

    def atualiza_resumo_do_pedido(self):
        total_pedido = sum(item['quantidade'] * item['valor'] for item in self.pedido)
        pedido_text = ''
        for item in self.pedido:
            total_item = item['quantidade'] * item['valor']
            pedido_text += f"{item['nome']} (ID: {item['id']}, {item['quantidade']}x R${item['valor']:.2f}) - Total: R${total_item:.2f}\n"
        pedido_text += f'Total do Pedido: R${total_pedido:.2f}'
        self.__window['pedido_text'].update(pedido_text)

    def criar_pedido(self, produtos):
        self.produtos = produtos
        layout = [
            [sg.Text('Selecione o produto:')],
            [sg.Listbox(
                [(f"{produto['nome']} (ID: {produto['id']}, R${produto['valor']:.2f})") for produto in produtos],
                size=(30, 6), key='produto_list')],
            [sg.Text('Quantidade:'), sg.InputText(key='quantidade')],
            [sg.Button('Adicionar Quantia Do Produto ao Pedido'), sg.Button('Retirar Produto do Pedido'), sg.Button('Concluir Pedido'),
             sg.Button('Voltar')],
            [sg.Text('Itens no Pedido:')],
            [sg.Multiline('', size=(40, 10), key='pedido_text', autoscroll=True)],
        ]

        self.__window = sg.Window('Criação de Pedido', layout)

        while True:
            event, values = self.__window.read()

            if event in (sg.WIN_CLOSED, 'Concluir Pedido', 'Voltar'):
                break

            # Adiciona
            elif event == 'Adicionar Quantia Do Produto ao Pedido':
                quantidade = values['quantidade'].strip()

                if not values['produto_list']:
                    sg.popup("Selecione um produto antes de adicionar ao pedido.")
                    continue
                elif not quantidade:
                    sg.popup("Digite a quantidade antes de adicionar ao pedido.")
                    continue
                elif not quantidade.isdigit() or int(quantidade) <= 0:
                    sg.popup("A quantidade deve ser um número inteiro positivo.")
                    continue
                else:
                    quantidade = int(quantidade)
                    produto_selecionado_str = values['produto_list'][0]
                    produto_selecionado = produto_selecionado_str.split(" (ID: ")[0]

                existing_product = next((item for item in self.pedido if item['nome'] == produto_selecionado), None)

                if existing_product:
                    existing_product['quantidade'] += quantidade
                else:
                    for produto in self.produtos:
                        if produto['nome'] == produto_selecionado:
                            self.pedido.append({
                                'id': produto['id'],
                                'nome': produto['nome'],
                                'quantidade': quantidade,
                                'valor': produto['valor']
                            })
                self.atualiza_resumo_do_pedido()

            # Retira
            elif event == 'Retirar Produto do Pedido':
                if not values['produto_list']:
                    sg.popup("Selecione um item do pedido para remover.")
                else:
                    item_to_remove = values['produto_list'][0]
                    item_to_remove_name = item_to_remove.split(" (ID: ")[0]
                    self.pedido = [item for item in self.pedido if item['nome'] != item_to_remove_name]
                    self.atualiza_resumo_do_pedido()

        # Final
        self.__window.close()
        return self.pedido, event


# if __name__ == '__main__':
#     produtos = [
#         {
#             "nome": "produto 1",
#             "id": 1,
#             "valor": 10.00,
#         },
#         {
#             "nome": "produto 2",
#             "id": 2,
#             "valor": 20.00,
#         },
#         {
#             "nome": "produto 3",
#             "id": 3,
#             "valor": 30.00,
#         },
#     ]
#     pedido = TelaPedido().criar_pedido(produtos)
