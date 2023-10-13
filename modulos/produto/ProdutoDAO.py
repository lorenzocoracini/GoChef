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
        
    def guardar(self):
        chaves = f"({','.join(self.atributos.keys())})"
        valores = tuple([v.identificador if isinstance(
            v, DAO) else v for v in self.atributos.values()])
        parametros = '('+','.join('?' for _ in valores)+')'

        print('nome da tabela =', self.nomeTabela)
        print('chaves', chaves)
        print('parametros', self.atributos)

        try:
            with self.conexao:
                self.cursor.execute(f"""
          INSERT INTO {self.nomeTabela}
          {chaves}
          VALUES {parametros}
        """, valores)
                return True
        except:
            raise Exception('Esse produto já foi adicionado!')

    @staticmethod
    def buscar() -> list | None:
        try:
            res = ProdutoDAO.cursor.execute(f'''
                SELECT *
                FROM {ProdutoDAO.nome_tabela}
            ''')
            return [dict(row) for row in res.fetchall()]
        except:
            return None