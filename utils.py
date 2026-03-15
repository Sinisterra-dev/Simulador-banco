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