from cuenta import Cuenta


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
    
    # 🔹 Guardar datos en JSON
    def guardar_datos(self):

        datos = {}

        for no_cuenta, cuenta in self.cuentas.items():

            datos[no_cuenta] = cuenta.to_dict()

        with open("cuentas.json", "w") as archivo:

            json.dump(datos, archivo, indent=4)