import re
import PySimpleGUI as sg
from modulos.produto.CategoriaProduto import CategoriaProduto

class TelaProduto:
    def __init__(self) -> None:
        sg.ChangeLookAndFeel('Material2')
        self.__window = None

    def trata_string(self, valor: str, nome_campo=None, min_len=None, max_len=None):
        valor_tratado = ' '.join(
            [palavra[0].upper() + palavra[1:] for palavra in valor.split()])
        if not valor_tratado:
            raise ValueError(f'Entrada inválida. {nome_campo} não pode ser vazio.')
        if re.search('\d', valor_tratado):
            raise ValueError(
                f'Entrada inválida. {nome_campo} não deve conter dígitos.')
        if min_len and len(valor_tratado) < min_len:
            raise ValueError(
                f'{nome_campo} deve ter no mínimo {min_len} caracteres!')
        if max_len and len(valor_tratado) > max_len:
            raise ValueError(
                f'{nome_campo} deve ter no máximo {max_len} caracteres!')

        return valor_tratado
        
    def valida_real(self, valor: str, nome_campo=None):
        try:
            return float(valor)
        except:
            erro = 'Por favor, insira um número real'
            if nome_campo:
                raise ValueError(erro + f' no campo {nome_campo}.')
            raise ValueError(erro + '.')
    
    def abre(self):
        return self.__window.Read()

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem_erro(self, mensagem: str) -> None:
        sg.popup_error(mensagem)

    def mostra_opcoes(self, produtos):
        column = []

        if len(produtos) == 0:
            column.append([sg.Text('Nenhum produto cadastrado')])
        else:
            for produto in produtos:
                column.append(
                    [
                        sg.Text(produto['nome'], key=produto['id']),
                        sg.Button(
                        'Editar', key=f'editar {produto["id"]}'),
                        sg.Button(
                        'Excluir', key=f'excluir {produto["id"]}'),
                    ]
                )

        layout = [
            [sg.Text('Produtos')],
            [sg.Column(column, key='lista_produtos')],
            [sg.Button('Voltar'), sg.Button('Adicionar')]
        ]

        self.__window = sg.Window('Produtos').Layout(layout)
        botao, valores = self.abre()

        if not botao:
            exit(0)

        while True:
            if botao == 'Voltar':
                self.fecha()
                return {
                    'voltar': True
                }
        
            if botao == 'Adicionar':
                self.fecha()
                return {
                    'adicionar': True
                }
            
            if 'editar' in botao:
                produto_id = botao.split()[1]
                return {
                    'editar': True,
                    'id': int(produto_id)
                }
           
            if 'excluir' in botao:
                produto_id = botao.split()[1]
                return {
                    'excluir': True,
                    'id': int(produto_id)
                }
            
    
    def pega_dados_novo_produto(self):
        categorias_produto = [
            categoria.name.capitalize() for categoria in CategoriaProduto
        ]

        layout = [
            [sg.Text('Adicionar produto')],
            [sg.Text('Nome', size=(15, 1)),
             sg.InputText(key='nome', default_text='')],
            [sg.Text('Valor', size=(15, 1)),
             sg.InputText(key='valor')],
            [sg.Text('Categoria', size=(15, 1)),
             sg.Combo(
                 categorias_produto, 
                 default_value=categorias_produto[0], 
                 key='categoria', 
                 readonly=True
                )
            ],
            [sg.Button('Voltar'), sg.Button('Adicionar')]
        ]

        self.__window = sg.Window('Adicionar Produto').Layout(layout)
        botao, valores = self.abre()

        if not botao:
            exit(0)

        while True:
            try:
                if botao == 'Voltar':
                    self.fecha()
                    return {
                        'voltar': True
                    }
            
                nome_produto = self.trata_string(valores['nome'], nome_campo='Nome do produto', min_len=3)
                valor_produto = self.valida_real(valores['valor'], nome_campo='valor do produto')
                categoria_produto = CategoriaProduto[valores['categoria'].upper()].value

                self.fecha()
                return {
                    'nome': nome_produto,
                    'valor': valor_produto,
                    'categoria': categoria_produto
                }
            except Exception as err:
                self.mostra_mensagem_erro(err)
                botao, valores = self.abre()