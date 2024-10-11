
from time import sleep
# funcion para hacer retiros ademas de que tambien guardamos toda la info de los movimientos
def debito(cuentas,movimientos,localtime):
    print("Bienvenido")
    print("Ingrese su documento")
    val_d = input("= ")
    print("Ingrese su clave")
    val_c = input("= ")

    for cuenta in cuentas:
            if cuenta["cc"] == val_d and cuenta["clave"] == val_c:
                print(f"La cuenta a la que va a retirar dinero es: {cuenta['cta']}")
                saldo =int(input(f"Ingrese el monto que desea retirar: $ "))
                #-----------------------------------------------------------------------
                if cuenta["saldo"] < saldo:
                     print("No tienes suficientes fondos para este retiro")
                     break
                elif saldo <= 0:
                     print("No puedes retirar un valor negativo o igual a cero")
                     break
                #-----------------------------------------------------------------------
                cuenta["saldo"] -= saldo
                for movimiento in movimientos:
                    if cuenta["cta"] == movimiento["cta"]:
                        movimiento["movimientos"].append({
                        "tipo": "retiro",
                        "referencia": "",
                        "descripcion": f"se ha retirado ${saldo}",
                        "saldo": f"${cuenta['saldo']}",
                        "fecha": f"{localtime()}",
                        })
                        print("Dinero retirado con exito!")
                    else:
                        print("Cuenta no encontrada")
            else:
                return print("No se encontro la cuenta")
