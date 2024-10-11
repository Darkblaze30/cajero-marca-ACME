#aqui hacemos el conteo de todos los movimientos y los mostramos

def mov(cuentas,movimientos):
    numeroCuenta = input("Digite el numero de su cuenta ")
    clave = input("Digite la contraseña de su cuenta ")
    for cuenta in cuentas:
        if cuenta["cta"] == numeroCuenta and cuenta["clave"] == clave:
            for movimiento in movimientos:
                if movimiento["cta"] == cuenta["cta"]:
                    print(movimiento["movimientos"])
        else:
            print("Codigo incorrecto")
