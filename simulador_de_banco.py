##Alexander Sinisterra Moreno
#Simulador de banco
#Nivel 2
import json 


class Cuenta:
    def __init__(self, no_cuenta, titular, saldo):
        # Inicializa una cuenta con número, titular, saldo e historial vacío
        self.no_cuenta = no_cuenta
        self.titular = titular
        self.saldo = saldo
        self.historial = []

    def depositar(self, monto):
        # Añade dinero a la cuenta y registra el movimiento
        if monto <= 0:
            print("Valor incorrexto, ingrese un valor correcto")
            return False
        else:
            self.saldo += monto
            self.historial.append(f"depósito {monto}")
            return True


    def retirar(self, valor):
        # Resta dinero de la cuenta si hay fondos suficientes
        
        if valor <= 0:
            print("Ingresa un valor a retirar válido.")
            return False

        elif valor > self.saldo:
            print("Fondos insuficientes")
            return False

        else:
            self.saldo -= valor
            self.historial.append(f"Retiro: {valor}")
            return True

    def ver_historial(self):
        # Muestra todos los movimientos realizados en la cuenta
        for movimiento in self.historial:
            print(movimiento) 

class Banco:

    def __init__(self):
        # Inicializa el banco con un diccionario vacío de cuentas
        self.cuentas = {}

    def crear_cuenta(self, no_cuenta, titular, saldo):
        # Crea una nueva cuenta si no existe
        if no_cuenta in self.cuentas:
            print("Cuenta ya existente")

        else:
            cuenta = Cuenta(no_cuenta, titular, saldo)
            self.cuentas[no_cuenta] = cuenta
    
    def depositar(self, no_cuenta, monto):
        # Realiza un depósito en una cuenta existente
        if no_cuenta in self.cuentas:
            self.cuentas[no_cuenta].depositar(monto)

        else:
            print("Cuenta no encontrada")
    
    def retirar(self, no_cuenta, monto):
        # Realiza un retiro en una cuenta existente
        if no_cuenta in self.cuentas:
            self.cuentas[no_cuenta].retirar(monto)
            

    def transferir(self, origen, destino, monto):

        if origen in self.cuentas and destino in self.cuentas:

            resultado = self.cuentas[origen].retirar(monto)

            if resultado:
                self.cuentas[destino].depositar(monto)

                self.cuentas[origen].historial.append(
                f"Transferencia enviada: -{monto} a cuenta {destino}"
                )

                self.cuentas[destino].historial.append(
                f"Transferencia recibida: +{monto} de cuenta {origen}"
                )

        else:
            print("Cuenta no encontrada")
            

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



    


