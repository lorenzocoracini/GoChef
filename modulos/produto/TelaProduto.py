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
            raise ValueError(f'Entrada inválida. O campo {nome_campo.lower()} não pode ser vazio.')
        if re.match(r'^\s*\d+(\s+\d+)*\s*$', valor_tratado):
            raise ValueError(
                f'Entrada inválida. O campo {nome_campo.lower()} não deve conter apenas dígitos e espaços.')
        if min_len and len(valor_tratado) < min_len:
            raise ValueError(
                f'Entrada inválida. O campo {nome_campo.lower()} deve ter no mínimo {min_len} caracteres.')
        if max_len and len(valor_tratado) > max_len:
            raise ValueError(
                f'Entrada inválida. O campo {nome_campo.lower()} deve ter no máximo {max_len} caracteres.')

        return valor_tratado
        
    def valida_real(self, valor: str, nome_campo=None):
        try:
            return float(valor)
        except:
            erro = 'Entrada inválida. '
            if nome_campo:
                raise ValueError(erro + f'O campo {nome_campo.lower()} deve ser um valor real.')
            raise ValueError(erro + 'Por favor, insira um número real.')
    
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
                        'Detalhes', key=f'detalhes {produto["id"]}'),
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
            
            if 'detalhes' in botao:
                self.fecha()
                produto_id = botao.split()[1]
                return {
                    'ver_detalhes': True,
                    'id': int(produto_id)
                }
            
            if 'editar' in botao:
                self.fecha()
                produto_id = botao.split()[1]
                return {
                    'editar': True,
                    'id': int(produto_id)
                }
           
            if 'excluir' in botao:
                self.fecha()
                produto_id = botao.split()[1]
                return {
                    'excluir': True,
                    'id': int(produto_id)
                }

    def mostra_detalhes(self, nome: str, categoria: str, valor: float):
        layout = [
            [sg.Text(f'- Nome: {nome}')],
            [sg.Text(f'- Categoria: {categoria}')],
            [sg.Text(f'- Valor: R${valor:.2f}')],
            [sg.Button('Voltar')]
        ]

        self.__window = sg.Window('Detalhes Produto').Layout(layout)
        botao, valores = self.abre()

        if not botao:
            exit(0)

        self.fecha()
        if botao == 'Voltar':
            return {
                'voltar': True
            }
    
    def confirma_exclusao_produto(self, categoria: str, nome: str):
        mensagem_confirmacao = f'''
            Você tem certeza que deseja excluir a {categoria} {nome}?
        '''
        layout = [
            [sg.Text(mensagem_confirmacao)],
            [sg.Button('Não'), sg.Button('Sim')]
        ]

        self.__window = sg.Window('Remover Produto').Layout(layout)
        botao, valores = self.abre()

        if not botao:
            exit(0)

        self.fecha()
        if botao == 'Não':
            return False
        return True
    
    def pega_valores_default_adiciona_produto(self):
        return {
            'titulo_tela': 'Adicionar produto',
            'nome': '',
            'valor': '',
            'categoria': 0
        }

    def pega_dados_produto(self, **kwargs):
        valores_iniciais = None

        if len(kwargs) == 0:
            valores_iniciais = self.pega_valores_default_adiciona_produto()
        else:
            valores_iniciais = kwargs
        
        categorias_produto = [
            categoria.name.capitalize() for categoria in CategoriaProduto
        ]

        layout = [
            [sg.Text('Nome', size=(15, 1)),
             sg.InputText(key='nome', default_text=valores_iniciais['nome'])],
            [sg.Text('Valor', size=(15, 1)),
             sg.InputText(key='valor', default_text=valores_iniciais['valor'])],
            [sg.Text('Categoria', size=(15, 1)),
             sg.Combo(
                 categorias_produto, 
                 default_value=categorias_produto[valores_iniciais['categoria']], 
                 key='categoria', 
                 readonly=True
                )
            ],
            [sg.Button('Voltar'), sg.Button(
                'Adicionar'
                if valores_iniciais['titulo_tela'] == 'Adicionar produto'
                else 'Editar'
            )]
        ]

        self.__window = sg.Window(valores_iniciais['titulo_tela']).Layout(layout)
        botao, valores = self.abre()

        while True:
            try:
                if not botao:
                    exit(0)

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