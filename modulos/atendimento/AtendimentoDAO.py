from erros.ErroEntradaVazia import ErroEntradaVazia
from abstrato.DAO import DAO
from modulos.pedido.PedidoDAO import PedidoDAO
import sqlite3
from erros.ErroValorUnico import ErroValorUnico


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
              mesa_id INTEGER NOT NULL,
              FOREIGN KEY (mesa_id) REFERENCES Mesa (id) ON DELETE RESTRICT
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

    def guardar(self):
        atributos = [
            key for key in self.atributos.keys() if key != 'pedidos']
        chaves = f"({','.join(atributos)})"
        valores = tuple([v.identificador if isinstance(
            v, DAO) else v for k, v in self.atributos.items() if k != 'pedidos'])
        parametros = '(' + ','.join('?' for _ in valores) + ')'

        try:
            with self.conexao:
                self.cursor.execute(f"""
             INSERT INTO {self.nome_tabela}
             {chaves}
             VALUES {parametros}
             """, valores)
                return True
        except sqlite3.IntegrityError:
            raise ErroValorUnico("Já existe uma atendimento com este número")
        except Exception:
            raise

    def buscar_pedidos(self) -> list:
        try:
            res = AtendimentoDAO.cursor.execute(
                f"""SELECT 
                  id
                FROM {PedidoDAO.nome_tabela} 
                WHERE atendimento_id = {self.identificador}""")
            return [dict(row) for row in res.fetchall()]
        except Exception as err:
            return
