# Determinar la suma de todos los númerosde 1 a N. N es un número que se ingresa por consola.


def suma_n(n):
    return int((n * (n + 1)) / 2)
    pass


numero = int(input("Ingrese un número: "))

print(suma_n(numero))
