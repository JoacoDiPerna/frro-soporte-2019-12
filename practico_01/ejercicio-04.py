# Escribir una función que tome un caracter y devuelva True si es una vocal, de lo contrario devuelve False.


def es_vocal(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
    pass


assert (es_vocal('a') is True)

assert (es_vocal('b') is False)
