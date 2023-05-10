from Banco.cuenta_bancaria import CuentaBancaria
from Banco.menu import menu_cuenta_bancaria

cuenta=CuentaBancaria(0)

opcion = menu_cuenta_bancaria()


if opcion == 1:
    monto = float (input("Ingrese el monto a depositar"))
    cuenta.depositar(monto)
elif opcion == 2:
    monto = float (input("Ingrese el monto a retirar"))
    monto = float (input("Ingrese el monto a retirar"))
    cuenta.retirar(monto)
elif opcion == 3:
    cuenta.consultar_saldos()
elif opcion == 4:
    print("Hasta luego")
    
    
