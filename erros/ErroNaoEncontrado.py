class ErroNaoEncontrado(Exception):
  def __init__(self) -> None:
    super().__init__('Não foi encontrado um objeto com este ID')