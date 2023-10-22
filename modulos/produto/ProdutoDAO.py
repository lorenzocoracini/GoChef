from abstrato.DAO import DAO


class ProdutoDAO(DAO):
    nome_tabela = 'Produto'

    def __init__(self) -> None:
        super().__init__('Produto', 'id')

    def criar(self):
        with self.conexao:
            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.nome_tabela} (
                id        INTEGER PRIMARY KEY,
                nome      TEXT,
                valor     FLOAT,
                categoria INTEGER,
                UNIQUE(nome, categoria)
            )
        ''')
            return True
        
    def atualizar(self, **kwargs):
        set_statement = ', '.join([f"{k} = '{v}'" for k, v in kwargs.items()])
        try:
            with self.conexao:
                self.cursor.execute(f"""
          UPDATE {self.nomeTabela} 
          SET {set_statement}
          WHERE {self.coluna_id} = '{self.identificador}'
        """)
                return True
        except Exception:
            raise Exception('Entrada inválida. Um produto com mesmo nome e mesma categoria já foi cadastrado no sistema.')
        
    def guardar(self):
        chaves = f"({','.join(self.atributos.keys())})"
        valores = tuple([v.identificador if isinstance(
            v, DAO) else v for v in self.atributos.values()])
        parametros = '('+','.join('?' for _ in valores)+')'

        try:
            with self.conexao:
                self.cursor.execute(f"""
          INSERT INTO {self.nomeTabela}
          {chaves}
          VALUES {parametros}
        """, valores)
                return True
        except:
            raise Exception('Entrada inválida. Um produto com mesmo nome e mesma categoria já foi cadastrado no sistema.')

    @staticmethod
    def buscar() -> list:
        try:
            res = ProdutoDAO.cursor.execute(f'''
                SELECT *
                FROM {ProdutoDAO.nome_tabela}
            ''')
            return [dict(row) for row in res.fetchall()]
        except:
            return None