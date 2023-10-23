import sqlite3
from erros.ErroValorUnico import ErroValorUnico
from erros.ErroEntradaVazia import ErroEntradaVazia
from abstrato.DAO import DAO
from modulos.atendimento.AtendimentoDAO import AtendimentoDAO


class MesaDAO(DAO):
    nome_tabela = 'Mesa'

    def __init__(self) -> None:
        super().__init__('Mesa', 'id')

    def criar(self):
        try:
            with self.conexao:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.nome_tabela} 
            (
              id INTEGER PRIMARY KEY, 
              numero_lugares INTEGER, 
              numero_mesa INTEGER UNIQUE
            )
        """)
            return True
        except Exception:
            raise
        
    def buscar_atendimentos(self) -> list:
        try:
            res = MesaDAO.cursor.execute(
                f"""SELECT 
                  id, 
                  data, 
                  encerrado, 
                  taxa_servico, 
                  valor_total 
                FROM {AtendimentoDAO.nome_tabela} 
                WHERE mesa_id = {self.identificador}""")
            return [dict(row) for row in res.fetchall()]
        except:
            return

    def guardar(self):
        atributos = [
            key for key in self.atributos.keys() if key != 'atendimentos']
        chaves = f"({','.join(atributos)})"
        valores = tuple([v.identificador if isinstance(
            v, DAO) else v for k, v in self.atributos.items() if k != 'atendimentos'])
        parametros = '('+','.join('?' for _ in valores)+')'

        try:
            with self.conexao:
                self.cursor.execute(f"""
            INSERT INTO {self.nome_tabela}
            {chaves}
            VALUES {parametros}
            """, valores)
                return True
        except sqlite3.IntegrityError:
            raise ErroValorUnico("Já existe uma mesa com este número")
        except Exception:
            raise

    def atualizar(self):
        set_statement = ', '.join([f"{k} = '{v}'" for k, v in self.atributos.items(
        ) if not isinstance(v, DAO) and v is not None])
        try:
            with self.conexao:
                self.cursor.execute(f"""
          UPDATE {self.nomeTabela} 
          SET {set_statement}
          WHERE {self.coluna_id} = '{self.identificador}'
        """)
                return True
        except sqlite3.IntegrityError:
            raise ErroValorUnico("Já existe uma mesa com este número")
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = MesaDAO.cursor.execute(
                f"SELECT * FROM {MesaDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except Exception as err:
            raise ErroEntradaVazia
