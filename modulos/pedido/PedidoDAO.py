from abstrato.DAO import DAO
from modulos.produto_pedido.ProdutoPedidoDAO import ProdutoPedidoDAO


class PedidoDAO(DAO):
    nome_tabela = 'Pedido'

    def __init__(self) -> None:
        super().__init__('Pedido', 'id')

    def criar(self):
        with self.conexao:
            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.nome_tabela} (
                id  TEXT PRIMARY KEY,
                atendimento_id INTEGER NOT NULL,
                FOREIGN KEY (atendimento_id) REFERENCES Atendimento (id) ON DELETE RESTRICT
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

    def buscar_produtos_pedidos_2(self, pedido_id) -> list:
        print(pedido_id, 'pedido_id')
        try:
            res = PedidoDAO.cursor.execute(
                f"""SELECT 
                  id, 
                  produto_id, 
                  quantidade
                FROM ProdutoPedido
                WHERE pedido_id = '{pedido_id}'""")
            ret = [dict(row) for row in res.fetchall()]
            return ret
        except Exception as err:
            return

    def buscar_produtos_pedidos(self) -> list:
        try:
            res = PedidoDAO.cursor.execute(
                f"""SELECT 
                  id, 
                  produto_id, 
                  quantidade,
                  pedido_id 
                FROM {ProdutoPedidoDAO.nome_tabela} 
                WHERE pedido_id = ?""", (self.identificador,))

            ret = [dict(row) for row in res.fetchall()]
            return ret
        except Exception as err:
            return

    def remover_pedido(self, id):
        try:
            with self.conexao:
                self.cursor.execute(f"""
          DELETE 
          FROM pedido
          WHERE id = '{id}'
        """)
                return True
        except Exception:
            raise

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
