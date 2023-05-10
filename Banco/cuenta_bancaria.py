class CuentaBancaria:
    def __init__(self,saldo_inicial) -> None:
        self.saldo = saldo_inicial
    def depositar(self,monto):
        self.saldo += monto
        print(f"Se deposito ${monto} en la cuenta. Saldo actual {self.saldo}")
    def retirar(self,monto):
        self.saldo -= monto
        print(f"Se retiro ${monto}. Saldo actual {self.saldo}")
    def consultar_saldos(self):
        print(f"Saldo actual {self.saldo}")
    def __str__(self) -> str:
        return f"El saldo actual es de ${self.saldo}"

