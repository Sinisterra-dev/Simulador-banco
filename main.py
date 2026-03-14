##Alexander Sinisterra Moreno
#Simulador de banco
#Nivel 2
import json 
from banco import Banco
from utils import pedir_entero, pedir_float, pedir_texto



def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un número válido")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingresa un número válido")


def pedir_texto(mensaje):
    texto = input(mensaje).strip()
    return texto

banco = Banco()

while True:
    print("\n--- BANCO ---")
    print("1. Crear cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Transferir")
    print("5. Ver historial")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        no_cuenta = pedir_entero("Número de cuenta: ")
        titular = pedir_texto("Nombre del titular: ")
        saldo = pedir_float("Saldo inicial: ")

        banco.crear_cuenta(no_cuenta, titular, saldo)

    elif opcion == "2":

        no_cuenta = pedir_entero("Número de cuenta: ")
        monto = pedir_float("Cantidad a ingresar:")

        banco.depositar(no_cuenta, monto)
    
    elif opcion == "3":

        no_cuenta = pedir_entero("Número de cuenta: ")
        monto = pedir_float("Cantidad a retirar:")

        banco.retirar(no_cuenta, monto)
    
    elif opcion == "4":

        origen = pedir_entero("Cuenta origen: ")
        destino = pedir_entero("Cuenta destino: ")
        monto = pedir_float("Monto a transferir: ")

        banco.transferir(origen,destino,monto)

    elif opcion == "5":

        no_cuenta = pedir_entero("Número de cuenta: ")
        if no_cuenta in banco.cuentas:
            banco.cuentas[no_cuenta].ver_historial()
    
        else:
            print("Número de cuenta no encontrada")

        

        
    
    elif opcion == "6":

        print("Saliendo del sistema...")
        break

    else:
        print("Número inválido ")



    


