from abstrato.DAO import DAO


class ProdutoDAO(DAO):
    nome_tabela = 'Produtos'

    def __init__(self) -> None:
        super().__init__('Produtos', 'id')

    def criar(self):
        try:
            with self.conexao:
                self.cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.nome_tabela} (
                    id    INTEGER PRIMARY KEY,
                    nome  TEXT,
                    valor FLOAT
                )
            ''')
                return True
        except:
            raise

    def buscar(self) -> list:
        try:
            res = self.cursor.execute(f'''
                SELECT *
                FROM {self.nome_tabela}
            ''')
            return [dict(row) for row in res.fetchall()]
        except:
            return None