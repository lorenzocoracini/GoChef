import random
from erros.ErroEntradaVazia import ErroEntradaVazia
from abstrato.DAO import DAO
from modulos.exemplo.professor.turno.TurnoDAO import TurnoDAO


class ProfessorDAO(DAO):
    nome_tabela = 'Professor'

    def __init__(self) -> None:
        super().__init__('Professor', 'id')

    def criar(self):
        try:
            with self.conexao:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.nomeTabela} 
            (
              id INTEGER PRIMARY KEY, 
              nome TEXT, 
              cpf TEXT, 
              peso INTEGER,
              altura REAL,
              salario TEXT
            )
        """)
            return True
        except Exception:
            raise

    def buscar_turnos(self) -> list:
        try:
            res = ProfessorDAO.cursor.execute(
                f"SELECT * FROM {TurnoDAO.nome_tabela} WHERE professor = {self.identificador}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise ErroEntradaVazia

    @staticmethod
    def buscar() -> list:
        try:
            res = ProfessorDAO.cursor.execute(
                f"SELECT * FROM {ProfessorDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise ErroEntradaVazia
