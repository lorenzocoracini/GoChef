from erros.ErroEntradaVazia import ErroEntradaVazia
from abstrato.DAO import DAO


class AtendimentoDAO(DAO):
    nome_tabela = 'Atendimento'

    def __init__(self) -> None:
        super().__init__('Atendimento', 'id')

    def criar(self):
        try:
            with self.conexao:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.nomeTabela} 
            (
              id INTEGER PRIMARY KEY, 
              data TEXT, 
              encerrado BOOL,
              taxa_servico REAL,
              valor_total REAL,
              mesa INTEGER NOT NULL,
              FOREIGN KEY (mesa) REFERENCES Mesa (id) ON DELETE RESTRICT
            )
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = AtendimentoDAO.cursor.execute(
                f"SELECT * FROM {AtendimentoDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise ErroEntradaVazia
