cuentas = []  # cc. nombre, clave, cuenta, saldo en 0

def validacion():

    print("Ingrese su documento")
    val_d = input("= ")
    print("Ingrese su clave")
    val_c = input("= ")

    for cuenta in cuentas:
            if cuenta["cc"] == val_d and cuenta["clave"] == val_c:
                return True
            return False