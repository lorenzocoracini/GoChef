from modulos.produto.TelaProduto import TelaProduto

class ControladorProduto:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()
        self.__produtos = []

    def abre_menu_produto(self):
        pass