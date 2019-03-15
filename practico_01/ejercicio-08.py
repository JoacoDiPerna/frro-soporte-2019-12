# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado.


def superposicion(lista1, lista2):
    for i in lista1:
        if i in lista2:
            return True
    return False
    pass


assert (superposicion(["i", "pedro", "sergio"], ["laura", "c", "manzana"]) is False)

assert (superposicion(["i", "pedro", "sergio"], ["laura", "c", "i"]) is True)
