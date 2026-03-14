
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
    
    def to_dict(self):
        return {
            "no_cuenta": self.no_cuenta,
            "titular": self.titular,
            "saldo": self.saldo,
            "historial": self.historial
        }
