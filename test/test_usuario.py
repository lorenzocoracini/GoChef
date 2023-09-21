import sqlite3
import unittest

from modulos.usuario.ControladorUsuario import ControladorUsuario

class TestUsuario(unittest.TestCase):
  connection = sqlite3.connect('test.db')
  connection.row_factory = sqlite3.Row 
  cursor = connection.cursor()
  controlador_mock = ControladorUsuario()

  def cadastrar(self):
    dados_mock = {
      "id": 123,
      "gerente": True,
      "senha": "123",
    }
    self.controlador_mock.cadastrar(dados_mock)
    res = self.cursor.execute(f"SELECT gerente FROM Usuario WHERE id = {dados_mock['id']}")
    result = dict(res.fetchone())
    return (dados_mock['gerente'], result['gerente'])
  
  def editar(self):
    dados_mock = {
      "senha": "125",
    }
    self.controlador_mock.editar(123, dados_mock)
    res = self.cursor.execute(f"SELECT * FROM Usuario WHERE id = 123")
    result = dict(res.fetchone())
    return (dados_mock['senha'], result['senha'])
  
  def test(self):
    self.assertEqual(*self.cadastrar())
    self.assertEqual(*self.editar())

if __name__ == '__main__':
  unittest.main()