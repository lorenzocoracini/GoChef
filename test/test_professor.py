import sqlite3
import unittest

from modulos.exemplo.professor.ControladorProfessor import ControladorProfessor

class TestProfessor(unittest.TestCase):
  conexao = sqlite3.connect('test.db')
  conexao.row_factory = sqlite3.Row 
  cursor = conexao.cursor()
  controlador_mock = ControladorProfessor()

  def cadastrar(self):
    dados_mock = {
      "id": 1234,
      "nome": 'Professor Teste',
      "cpf": "000.000.000-00",
      "peso": 56,
      "altura": 1.70,
      "salario": 1750.99,
    }
    turnos_mock = [
        {"dia_semana": 'Segunda Feira', 'periodo': 'Manhã', "carga_horaria": 4, "professor": 1234}
      ]
    
    self.controlador_mock.cadastrar(dados_mock, turnos_mock)
    res = self.cursor.execute(f"SELECT nome FROM Professor WHERE id = {dados_mock['id']}")
    result = dict(res.fetchone())
    return (dados_mock['nome'], result['nome'])
  
  def editar(self):
    dados_mock = {
      "id": 1234,
      "nome": 'Professor Editado',
      "cpf": "111.111.111-11",
      "peso": 60,
      "altura": 1.70,
      "salario": 2542.75
    }
    turnos_mock = [
      {"dia_semana": 'Segunda Feira', 'periodo': 'Manhã', "carga_horaria": 4, "professor": 1234}
    ]
    self.controlador_mock.editar(dados_mock['id'], dados_mock, turnos_mock)
    res = self.cursor.execute(f"SELECT * FROM Professor WHERE id = {dados_mock['id']}")
    result = dict(res.fetchone())
    result['salario'] = float(result['salario'])
    return (dados_mock, result)
  
  def deletar(self):
    dados_mock = { "id": 1234 }
    self.controlador_mock.deletar(dados_mock['id'])
    res = self.cursor.execute(f"SELECT * FROM Professor WHERE id = {dados_mock['id']}")
    result = res.fetchone()
    return (None, result)
  
  def test(self):
    self.assertEqual(*self.cadastrar())
    self.assertEqual(*self.editar())
    self.assertEqual(*self.deletar())

if __name__ == '__main__':
  unittest.main()