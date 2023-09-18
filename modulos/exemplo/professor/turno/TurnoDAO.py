import random
from abstrato.DAO import DAO
from erros.ErroEntradaVazia import ErroEntradaVazia


class TurnoDAO(DAO):
    nome_tabela = 'Turno'

    def __init__(self) -> None:
        super().__init__('Turno', 'id')

    def criar(self):
        try:
            with self.conexao:
                self.cursor.executa(f"""
          CREATE TABLE IF NOT EXISTS {self.nomeTabela}
            (
              id INTEGER PRIMARY KEY,
              dia_semana TEXT,
              periodo TEXT,
              carga_horaria INTEGER NOT NULL,
              professor INTEGER NOT NULL,
              FOREIGN KEY (professor) REFERENCES Professor (id) ON DELETE CASCADE)
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = TurnoDAO.cursor.executa(
                f"SELECT * FROM {TurnoDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise ErroEntradaVazia
