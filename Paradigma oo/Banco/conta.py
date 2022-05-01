class Conta:
  def __init__(self, numero, titular, saldo, limite):
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite

  @property
  def saldo(self):
    return self.__saldo
  
  property
  def titular(self):
    return self.__titular

  @property
  def limite(self):
    return self.__limite


  @limite.setter
  def limite(self, limite):
    self.__limite = limite


  def extrato(self):
    print("\n==", end='')
    print('>EXTRATO<', end='')
    print("==")

    print(f'Titular: {self.__titular}')
    print(f'Saldo: {self.__saldo}')

    print("=" * 13)

  def depositar(self, valor):
    self.__saldo += valor
  
  def __pode_sacar(self, valor_a_sacar):
    valor_disponivel_a_sacar = self.saldo + self.limite

    return valor_a_sacar <= valor_disponivel_a_sacar

  def sacar(self, valor):
    if(self.__pode_sacar(valor)):
      self.__saldo -= valor

  def transferir(self, valor, conta):
    self.sacar(valor)
    conta.depositar(valor)

  @staticmethod
  def codigo_banco():
    return "001"