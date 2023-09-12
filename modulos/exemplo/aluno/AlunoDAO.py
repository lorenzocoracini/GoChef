import random
from erros.ErroEntradaVazia import ErroEntradaVazia
from abstrato.DAO import DAO


class AlunoDAO(DAO):
    nome_tabela = 'Aluno'

    def __init__(self) -> None:
        super().__init__('Aluno', 'id')

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
              data_matricula TEXT
            )
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = AlunoDAO.cursor.execute(
                f"SELECT * FROM {AlunoDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise ErroEntradaVazia
