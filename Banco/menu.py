from .validaciones import validar_opcion
# Crear un menú de opciones para Cuenta Bancariaclass Menu(CuentaBancaria)
def menu_cuenta_bancaria():
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Salir")
    opcion = int(input("ingrese una opción: "))
    validacion = validar_opcion(opcion)
    return validacion

a = menu_cuenta_bancaria()
print(a)


