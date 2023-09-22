from erros.ErroEntradaVazia import ErroEntradaVazia
from abstrato.DAO import DAO


class RestauranteDAO(DAO):
    nome_tabela = 'Restaurante'

    def __init__(self) -> None:
        super().__init__('Restaurante', 'id')

    def criar(self):
        try:
            with self.conexao:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.nomeTabela} 
            (
              id INTEGER PRIMARY KEY, 
              capacidade_maxima INTEGER
            )
        """)
            return True
        except Exception:
            raise

    def guardar(self):
        atributos = [
            key for key in self.atributos.keys() if key != 'cidades']
        chaves = f"({','.join(atributos)})"
        valores = tuple([v.identificador if isinstance(
            v, DAO) else v for k, v in self.atributos.items() if k != 'cidades'])
        parametros = '('+','.join('?' for _ in valores)+')'

        try:
            with self.conexao:
                self.cursor.execute(f"""
            INSERT OR IGNORE INTO {self.nomeTabela}
            {chaves}
            VALUES {parametros}
            """, valores)
                return True
        except Exception:
            raise

    def atualizar(self):
        set_statement = ', '.join([f"{k} = '{v}'" for k, v in self.atributos.items(
        ) if not isinstance(v, DAO) and v is not None and k != 'cidades'])
        try:
            with self.conexao:
                self.cursor.execute(f"""
        UPDATE {self.nomeTabela} 
        SET {set_statement}
        WHERE {self.coluna_id} = '{self.identificador}'
        """)
                return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = RestauranteDAO.cursor.execute(
                f"SELECT * FROM {RestauranteDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except:
            return None
