class InputInvalido(Exception):
  def __init__(self) -> None:
    super().__init__('Entrada inválida. Por favor respeite as restrições de entrada.')