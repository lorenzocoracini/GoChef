from modulos.produto.TelaProduto import TelaProduto
from modulos.produto.EntidadeProduto import Produto

class ControladorProduto:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__produtos = None
        self.carregar_dados_produtos()

    def carregar_dados_produtos(self):
        dados_produtos = Produto.buscar()
        if dados_produtos is None:
            self.__produtos = []
            return
        
        self.__produtos = [
            Produto(**produto) 
            for produto in dados_produtos
        ]

    def pega_dados_produtos(self):
        return [
            {
                'nome': produto.nome,
                'id': produto.identificador,
                'valor': produto.valor
            } for produto in self.__produtos
        ]

    def adiciona_produto(self):
        while True:
            try:
                novo_produto = self.__tela_produto.pega_dados_novo_produto()

                while 'voltar' not in novo_produto:
                    produto = Produto(**novo_produto)
                    produto.guardar()
                    self.carregar_dados_produtos()
                    novo_produto = self.__tela_produto.pega_dados_novo_produto()
                
                return self.abre_menu_produto()
            except Exception as err:
                self.__tela_produto.mostra_mensagem_erro(err)

    def edita_produto(self, id: int):
        print('edita produto', id)

    def exclui_produto(self, id: int):
        print('exclui produto', id)

    def abre_menu_produto(self):
        produtos = self.pega_dados_produtos()
        res = self.__tela_produto.mostra_opcoes(produtos)

        if 'adicionar' in res:
            return self.adiciona_produto()
        
        if 'editar' in res:
            return self.edita_produto(res['id'])
        
        if 'id' in res:
            return self.exclui_produto(res['id'])
        
        if 'voltar' in res:
            return self.__controlador_sistema.abre_menu_principal_gerente()