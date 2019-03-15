# Determinar la cantidad de dígitos de un número ingresado.


def cantidad_digitos(numero):
    contador = 1
    control = 10

    while control <= numero:
        contador = contador + 1
        control = control * 10
    return contador
    pass


assert (cantidad_digitos(0) == 1)

assert (cantidad_digitos(10) == 2)

assert (cantidad_digitos(99999) == 5)
