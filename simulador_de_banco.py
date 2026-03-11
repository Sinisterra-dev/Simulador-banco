##Alexander Sinisterra Moreno
#Simulador de banco


class Cuenta:
    def __init__(self, no_cuenta, titular, saldo):

        self.no_cuenta = no_cuenta
        self.titular = titular
        self.saldo = saldo
        self.historial = []

    def depositar(self, monto):

        if monto > 0:
            self.saldo += monto
            self.historial.append(f"depósito {monto}")


    def retirar(self, valor):

        if valor <= 0:
            print("Ingresa un valor a retirar válido.")

        elif valor > self.saldo:
            print("Fondos insuficientes")

        else:
            self.saldo -= valor
            self.historial.append(f"Retiro: {valor}")

    def ver_historial(self):

        for movimiento in self.historial:
            print(movimiento) 

class Banco:

    def __init__(self):

        self.cuentas = {}

    def crear_cuenta(self, no_cuenta, titular, saldo):
        

        if no_cuenta in self.cuentas:
            print("Cuenta ya existente")

        else:
            cuenta = Cuenta(no_cuenta, titular, saldo)
            self.cuentas[no_cuenta] = cuenta
   