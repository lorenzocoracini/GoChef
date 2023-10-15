from modulos.atendimento.ControladorAtendimento import ControladorAtendimento
from modulos.mesa.ControladorMesa import ControladorMesa
from modulos.usuario.ControladorUsuario import ControladorUsuario
from modulos.usuario.EntidadeUsuario import Usuario
from modulos.restaurante.ControladorRestaurante import ControladorRestaurante
from modulos.sistema.TelaSistema import TelaSistema
from modulos.produto.ControladorProduto import ControladorProduto
from modulos.pedido.ControladorPedido import ControladorPedido


class ControladorSistema:
    def __init__(self):
        self.__tela = TelaSistema()
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_restaurante = ControladorRestaurante(self)
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_pedido = ControladorPedido(self)
        self.__controlador_atendimento = ControladorAtendimento(self, self.__controlador_pedido)
        self.__controlador_mesa = ControladorMesa(self, self.__controlador_atendimento)
        self.usuario_atual_eh_gerente = None

    def __criar_usuarios(self):
        try:
            usuarios = Usuario.buscar()
        except:
            self.__controlador_usuario.cadastrar(
                {"gerente": True, "senha": "123"})
            self.__controlador_usuario.cadastrar(
                {"gerente": False, "senha": "123"})
            return

        if len(usuarios) == 0:
            self.__controlador_usuario.cadastrar(
                {"gerente": True, "senha": "123"})
            self.__controlador_usuario.cadastrar(
                {"gerente": False, "senha": "123"})

    def inicializa_sistema(self):
        self.__criar_usuarios()
        try:
            self.__controlador_restaurante.carrega_dados_restaurante()
        except:
            self.__controlador_restaurante.cadastrar_dados_iniciais()
        self.__controlador_usuario.cadastrar_senha()
        eh_gerente = self.__controlador_usuario.login()
        self.usuario_atual_eh_gerente = eh_gerente
        if eh_gerente:
            self.abre_menu_principal_gerente()
        else:
            self.abre_menu_principal_funcionario()

    def encerrar(self):
        exit(0)

    def lotacao_maxima_restaurante(self) -> int:
        return self.__controlador_restaurante.restaurante.capacidade_maxima

    def alterar_dados_restaurante(self):
        self.__controlador_restaurante.atualizar_dados()

    def alterar_senhas_sistema(self):
        self.__controlador_usuario.atualizar_senhas()

    def cadastrar_produtos(self):
        self.__controlador_produto.abre_menu_produto()

    def listar_mesas(self):
        self.__controlador_mesa.listar_mesas()

    def abre_menu_principal_gerente(self):
        switcher = {
            1: self.alterar_dados_restaurante,
            2: self.alterar_senhas_sistema,
            3: self.cadastrar_produtos,
            4: self.listar_mesas,
            0: self.encerrar
        }

        while True:
            switcher[self.__tela.mostra_opcoes_gerente()]()

    def abre_menu_principal_funcionario(self):
        switcher = {
            0: self.encerrar,
            1: self.listar_mesas,
        }

        while True:
            switcher[self.__tela.mostra_opcoes_funcionario()]()
