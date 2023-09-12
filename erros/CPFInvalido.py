class CPFInvalido(Exception):
  def __init__(self) -> None:
    super().__init__('CPF inválido. Por favor insira o CPF no formato 000.000.000-00')