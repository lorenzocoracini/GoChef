from erros.ErroEntradaVazia import ErroEntradaVazia
from abstrato.DAO import DAO


class UsuarioDAO(DAO):
    nome_tabela = 'Usuario'

    def __init__(self) -> None:
        super().__init__('Usuario', 'id')

    def criar(self):
        try:
            with self.conexao:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.nomeTabela} 
            (
              id INTEGER PRIMARY KEY, 
              gerente BOOL, 
              senha TEXT
            )
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = UsuarioDAO.cursor.execute(
                f"SELECT * FROM {UsuarioDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise ErroEntradaVazia
