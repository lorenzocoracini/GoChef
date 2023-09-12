from abc import ABC, abstractmethod
import sqlite3


class DAO(ABC):
    conexao = sqlite3.connect('test.db')
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    @abstractmethod
    def __init__(self, name: str, coluna_id: str) -> None:
        self.coluna_id = coluna_id
        self.nomeTabela = name
        self.conexao = DAO.conexao
        self.cursor = DAO.cursor
        self.criar()

    @property
    def atributos(self) -> dict:
        attributos_classe = {
            k.replace(f'_{self.nomeTabela}__', ''): v
            for k, v in self.__dict__.items() if k.startswith(f'_{self.nomeTabela}') and not k.endswith('_')
        }
        super_class = self.__class__.__base__.__name__
        if super_class != 'DAO':
            atributos_super = {
                k.replace(f'_{super_class}__', ''): v
                for k, v in self.__dict__.items() if k.startswith(f'_{super_class}')
            }
            attributos_classe = {**attributos_classe, **atributos_super}
        return attributos_classe

    @property
    @abstractmethod
    def identificador(self):
        ''' GETTER: Deve retornar o valor da propriedade identificadora da instancia '''

    @abstractmethod
    def criar(self):
        ''' Deve criar a cláusula para criar a tabela '''

    @staticmethod
    @abstractmethod
    def buscar():
        ''' DEVE FAZER UM SELECT ALL NA TABELA DA DAO '''

    def guardar(self):
        chaves = f"({','.join(self.atributos.keys())})"
        valores = tuple([v.identificador if isinstance(
            v, DAO) else v for v in self.atributos.values()])
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
        ) if not isinstance(v, DAO) and v is not None])

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

    def remover(self):
        try:
            with self.conexao:
                self.cursor.execute(f"""
          DELETE 
          FROM {self.nomeTabela}
          WHERE {self.coluna_id} = '{self.identificador}'
        """)
                return True
        except Exception:
            raise

    def __eq__(self, other):
        if self.identificador == other.identificador:
            return True
        else:
            return False
