# Escribir una función multip() que multiplique respectivamente todos los números de una lista.
# Por ejemplo: multip([1,2,3,4]) deberá devolver 24.

def multip(lista):
    retorno = 1
    for i in range(0, len(lista)):
        retorno = retorno * lista[i]
    return retorno
    pass


assert (multip([1, 6, 3]) == 18)

assert (multip([1, 2, 3]) == 6)
