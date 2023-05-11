def validar_opcion(opcion:str):
    if opcion.isdecimal():
        opcion_entero = int(opcion)
        if opcion_entero >= 1 and opcion_entero <= 4:
            return opcion_entero
    return False