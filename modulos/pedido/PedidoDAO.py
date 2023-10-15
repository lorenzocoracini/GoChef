from abstrato.DAO import DAO


class PedidoDAO(DAO):
    nome_tabela = 'Pedido'

    def __init__(self) -> None:
        super().__init__('Pedido', 'id')

    def criar(self):
        with self.conexao:
            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.nome_tabela} (
                id  INTEGER PRIMARY KEY
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
            raise Exception('Esse pedido já foi adicionado!')

    def guardar(self):
        atributos = [
            key for key in self.atributos.keys() if key != 'produtos_pedidos']
        chaves = f"({','.join(atributos)})"
        valores = tuple([v.identificador if isinstance(
            v, DAO) else v for k, v in self.atributos.items() if k != 'produtos_pedidos'])
        parametros = '(' + ','.join('?' for _ in valores) + ')'

        try:
            with self.conexao:
                sql = f"""
                       INSERT INTO {self.nomeTabela} {chaves}
                       VALUES {parametros}
                   """
                self.cursor.execute(sql, valores)
                return True
        except Exception as err:
            print("print-----", err)
            print("Generated SQL:", sql)
            raise Exception('Esse pedido já foi adicionado!')

    @staticmethod
    def buscar() -> list:
        try:
            res = PedidoDAO.cursor.execute(f'''
                    SELECT *
                    FROM {PedidoDAO.nome_tabela}
                ''')
            return [dict(row) for row in res.fetchall()]
        except:
            return None
