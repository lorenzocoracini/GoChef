from modulos.produto.TelaProduto import TelaProduto
from modulos.produto.EntidadeProduto import Produto
from modulos.produto.CategoriaProduto import CategoriaProduto

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

    def pega_produto_por_id(self, id: int) -> Produto:
        return [
            produto 
            for produto in self.__produtos 
            if produto.identificador == id
        ][0]

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
                novo_produto = self.__tela_produto.pega_dados_produto()

                while 'voltar' not in novo_produto:
                    produto = Produto(**novo_produto)
                    produto.guardar()
                    self.carregar_dados_produtos()
                    novo_produto = self.__tela_produto.pega_dados_produto()
                
                return self.abre_menu_produto()
            except Exception as err:
                self.__tela_produto.mostra_mensagem_erro(err)

    def edita_produto(self, id: int):
        print('edita produto', id)
        produto_a_editar = self.pega_produto_por_id(id)


    def exclui_produto(self, id: int):
        produto_a_excluir = self.pega_produto_por_id(id)
        if not self.__tela_produto.confirma_exclusao_produto(
            CategoriaProduto(produto_a_excluir.categoria).name.lower(),
            produto_a_excluir.nome
        ):
            return self.abre_menu_produto()
        
        produto_a_excluir.remover()
        self.carregar_dados_produtos()
        self.abre_menu_produto()

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