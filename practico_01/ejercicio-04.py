# Escribir una funciÃ³n que tome un carÃ¡cter y devuelva True si es una vocal, de lo contrario devuelve False.


def es_vocal(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
    pass


assert (es_vocal('a') is True)

assert (es_vocal('b') is False)
