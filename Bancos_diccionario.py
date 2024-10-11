cuentas = []  # cc. nombre, clave, cuenta, saldo en 0
movimientos = [] 

from Modulos_cajero.menu import *
from Modulos_cajero.creacion import *
from Modulos_cajero.Consignacion import *
from Modulos_cajero.retiro import *
from Modulos_cajero.pago_serv import *
from Modulos_cajero.movimientos import *


from time import asctime

#========================== VALIDACION =====================================


#========================== Inicio del programa ============================

while True:



    menu(asctime)

    eleccion = input("Escoja una opcion : ")

    if eleccion == "1":        
        creacion(cuentas,movimientos)

    elif eleccion == "2":

        consignacion(cuentas,movimientos,asctime)
    
    elif eleccion == "3":
        debito(cuentas,movimientos,asctime)        

    elif eleccion == "4":
        pago_servicio(cuentas,movimientos,asctime)      

    elif eleccion == "5":
       mov(cuentas,movimientos)

    elif eleccion == "6":
       print("Gracias por usar el programa")
       break    