from Banco.cuenta_bancaria import CuentaBancaria
# Crear un menú de opciones para Cuenta Bancariaclass Menu(CuentaBancaria)
def menu_cuenta_bancaria(self):
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Mostrar salir")
    opcion = int(input("ingrese una opción: "))
    return opcion

