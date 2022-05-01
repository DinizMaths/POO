from conta import Conta

conta = Conta(1, "Jão", 55.00, 100.00)

conta.extrato()

conta.depositar(200.00)
conta.extrato()

conta.sacar(100.00)
conta.extrato()