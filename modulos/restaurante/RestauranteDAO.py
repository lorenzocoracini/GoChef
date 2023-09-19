from erros.ErroEntradaVazia import ErroEntradaVazia
from abstrato.DAO import DAO


class RestauranteDAO(DAO):
    nome_tabela = 'Restaurante'

    def __init__(self) -> None:
        super().__init__('Restaurante', 'id')

    def criar(self):
        try:
            with self.conexao:
                self.cursor.executa(f"""
          CREATE TABLE IF NOT EXISTS {self.nomeTabela} 
            (
              id INTEGER PRIMARY KEY, 
              capacidade_maxima INTEGER,
            )
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = RestauranteDAO.cursor.executa(
                f"SELECT * FROM {RestauranteDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except:
            raise ErroEntradaVazia
