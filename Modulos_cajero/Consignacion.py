

def consignacion(cuentas,movimientos,localtime):
    
    print ("Ingrese su numero de cuenta o numero de documento ")
    cc = input(" = ")
    for cuenta in cuentas:
      if cuenta["cc"] == cc or cuenta["cta"] == cc:
       print(f"La cuenta a la que va a ingresar el cuenta es {cuenta['cta']}")
       saldo =int(input(f"Digite el monto que desea ingresar = $ "))
       #-----------------------------------------------------------------------
       if saldo <= 0:
        print("No puedes retirar un valor negativo o igual a cero")
        break
       #-----------------------------------------------------------------------
       cuenta["saldo"] += saldo
       for movimiento in movimientos:
         if cuenta["cta"] == movimiento["cta"]:
            movimiento["movimientos"].append({
              "tipo": "consignacion",
              "referencia": "",
              "descripcion": f"se ha consignado ${saldo}",
              "saldo": f"${cuenta['saldo']}",
              "fecha": f"{localtime()}",             
            })
            print("Dinero consigando con exito!")
      else:
        print("Cuenta no encontrada")