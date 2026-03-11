##Alexander Sinisterra Moreno
#Simulador de banco


class Cuenta:
    def __init__(self, no_cuenta, titular, saldo):
        # Inicializa una cuenta con número, titular, saldo e historial vacío
        self.no_cuenta = no_cuenta
        self.titular = titular
        self.saldo = saldo
        self.historial = []

    def depositar(self, monto):
        # Añade dinero a la cuenta y registra el movimiento
        if monto > 0:
            self.saldo += monto
            self.historial.append(f"depósito {monto}")


    def retirar(self, valor):
        # Resta dinero de la cuenta si hay fondos suficientes
        if valor <= 0:
            print("Ingresa un valor a retirar válido.")

        elif valor > self.saldo:
            print("Fondos insuficientes")

        else:
            self.saldo -= valor
            self.historial.append(f"Retiro: {valor}")

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
        # Transfiere dinero de una cuenta a otra
        if origen in self.cuentas and destino in self.cuentas:

            self.cuentas[origen].retirar(monto)
            self.cuentas[destino].depositar(monto)

        else:
            print("Cuenta no encontrada")
