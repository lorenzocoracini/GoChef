import random

# from erros.ErroEntradaVazia import ErroEntradaVazia
# from erros.ErroNaoEncontrado import ErroNaoEncontrado

from modulos.restaurante.EntidadeRestaurante import Restaurante
from modulos.restaurante.TelaRestaurante import TelaRestaurante


class ControladorRestaurante:
    def __init__(self):
        self.__tela = TelaRestaurante()
        self.__restaurante = None
        try:
            self.carregar_dados()
        except:
            self.incluir_restaurante()

    @property
    def restaurante(self):
        return self.__restaurante

    @restaurante.setter
    def restaurante(self, restaurante):
        self.__restaurante = restaurante

    def carregar_dados(self) -> None:
        dados_restaurante = Restaurante.buscar()
        if dados_restaurante is None:
            raise Exception

        self.__restaurante = Restaurante(**dados_restaurante)
        # for dados in dados_restaurante:
        #   objeto = Professor(**dados)
        #   turnos = objeto.buscar_turnos()
        #   objeto.turnos = turnos
        #   self.colecao.append(objeto)

    def incluir_restaurante(self):
        dados = self.__tela.mostra_opcoes('Informações do Restaurante')
        novo_restaurante = Restaurante(int(dados['capacidade_maxima']))
        novo_restaurante.guardar()
        self.carregar_dados()

    def abre_tela():
        pass

    # def cadastrar(self, dados: dict, turnos: list):
        # try:
        #     novo_professor = Professor(**dados)
        #     novo_professor.guardar()
        #     self.cadastrar_turno(novo_professor.identificador, turnos)
        #     self.carregar_dados()
        # except:
        #     raise ValueError


#   def editar(self, id, dados: dict, turnos: list):
#     try:
#       [objeto, _] = self.buscar_por_id(id)
#       for chave, valor in dados.items():
#         setattr(objeto, chave, valor)
#       objeto.atualizar()
#       for turno in turnos:
#         turno_editado = Turno(**turno)
#         turno_editado.atualizar()
#     except (ErroEntradaVazia, ErroNaoEncontrado):
#       raise
#     except:
#       raise ValueError

    # def deletar(self, id):
        # try:
        #     [objeto, _] = self.buscar_por_id(id)
        #     objeto.remover()
        #     self.carregar_dados()
        # except ErroNaoEncontrado:
        #     raise ErroNaoEncontrado
        # except:
        #     raise ValueError

    # def cadastrar_turno(self, identificador, turnos):
        # for turno in turnos:
        #     turno["professor"] = identificador
        #     turno["id"] = random.randint(1000, 9999)
        #     novo_turno = Turno(**turno)
        #     novo_turno.guardar()
        #     self.carregar_dados()

    # def deletar_turno(self, id):
        # try:
        #     turno = Turno('', '', 0, 0, id)
        #     turno.remover()
        #     self.carregar_dados()
        # except:
        #     raise ValueError

    # def buscar_por_id(self, id):
        # Recebe um id, busca ele na lista e devolve o objeto e o indice
        # if not len(self.colecao):
        #     raise ErroEntradaVazia
        # try:
        #     index = [x.identificador for x in self.colecao].index(id)
        # except ValueError:
        #     raise ErroNaoEncontrado
        # objeto = self.colecao[index]
        # return (objeto, index)

# if __name__ == '__main__':
    # ControladorRestaurante()
