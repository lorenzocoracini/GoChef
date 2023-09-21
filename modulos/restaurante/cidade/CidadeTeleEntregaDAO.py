from abstrato.DAO import DAO
# from erros.ErroEntradaVazia import ErroEntradaVazia


class CidadeTeleEntregaDAO(DAO):
    nome_tabela = 'CidadeTeleEntrega'

    def __init__(self) -> None:
        super().__init__('CidadeTeleEntrega', 'nome')

    # def criar(self):
    #     try:
    #         with self.conexao:
    #             self.cursor.execute(f"""
    #       CREATE TABLE IF NOT EXISTS {self.nomeTabela}
    #         (
    #           nome TEXT PRIMARY KEY,
    #           restaurante_id INTEGER NOT NULL,
    #           FOREIGN KEY (restaurante_id) REFERENCES Restaurante (id) ON DELETE CASCADE)
    #     """)
    #         return True
    #     except Exception:
    #         raise

    def guardar(self, restaurante_id: int):
        chaves = f"({','.join([*self.atributos.keys(), 'restaurante_id'])})"
        valores = tuple([v.identificador if isinstance(
            v, DAO) else v for v in [*self.atributos.values(), restaurante_id]])
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

    def criar(self):
        try:
            with self.conexao:
                self.cursor.execute(f"""
          CREATE TABLE IF NOT EXISTS {self.nomeTabela}
            (
              nome TEXT PRIMARY KEY,
              restaurante_id INTEGER NOT NULL,
              FOREIGN KEY (restaurante_id) REFERENCES Restaurante (id) ON DELETE CASCADE
            )
        """)
            return True
        except Exception:
            raise

    @staticmethod
    def buscar() -> list:
        try:
            res = CidadeTeleEntregaDAO.cursor.execute(
                f"SELECT * FROM {CidadeTeleEntregaDAO.nome_tabela}")
            return [dict(row) for row in res.fetchall()]
        except:
            return None
