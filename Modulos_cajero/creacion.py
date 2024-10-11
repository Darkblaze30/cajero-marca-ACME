from time import sleep
#esta funcion crea un diccionario para el usuario y uno tambien para sus movimientos
def creacion (cuentas,movimientos):
        cta = len(cuentas)+1                       #funcion para determinar el numero de cuentas hechas y asi asignar el numero de cuenta
        cuentas.append({                           #se le suma uno para que la primera no sea de 0
            "cc": input("Ingrese su documento: "), 
            "Name": input("Ingrese su nombre de usuario: "), 
            "clave": input("Ingrese su clave: "), 
            "cta": str(cta), 
            "saldo": 0})
        movimientos.append({
            "cta": f"{cta}",
            "movimientos": []
        })
        print("Creando cuenta")
        print("Espere un momento ...")
        sleep(1)
        print("Su cuenta fue creada con exito")
        print(f"Su numero de cuenta es: {cta}")
        print("Su saldo actual es de $ 0")
