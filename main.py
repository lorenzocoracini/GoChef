import sys
from abstrato.tela import Tela
from modulos.exemplo.aluno.ControladorAluno import ControladorAluno
from modulos.exemplo.aluno.TelaAluno import TelaAluno
from modulos.exemplo.professor.ControladorProfessor import ControladorProfessor
from modulos.exemplo.professor.TelaProfessor import TelaProfessor

controladorAluno = ControladorAluno()
controladorProfessor = ControladorProfessor()

telaAluno = TelaAluno(controladorAluno)
telaProfessor = TelaProfessor(controladorProfessor)

class TelaPrincipal(Tela):
    def __init__(self, titulo, objeto, opcoes, controlador):
        super().__init__(titulo, objeto, opcoes, controlador)

    def menu_principal(self):
        telas = {
            1: ['Tela de Alunos', telaAluno.mostrar_opcoes],
            2: ['Tela de Professores', telaProfessor.mostrar_opcoes],
            3: ['Sair', sys.exit]
        }
        print('\n-- GO CHEF --\n')
        for opcao, tela in telas.items():
            print(f"{opcao} - {tela[0]}")
        opcao_escolhida = self.inserir_inteiro(
            'Escolha uma tela: ', list(telas.keys()))
        telas[opcao_escolhida][1]()


if __name__ == "__main__":
    rodando = True
    tela = TelaPrincipal('GO CHEF', None, None, None)
    while rodando:
        tela.menu_principal()
