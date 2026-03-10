##Alexander Sinisterra Moreno
#Simulador de banco


class Cuenta:
    def __init__(self, no_cuenta, titular, saldo):

        self.no_cuenta = no_cuenta
        self.titular = titular
        self.saldo = saldo
        self.historial = []