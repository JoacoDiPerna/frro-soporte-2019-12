# Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".


def inversa(string):
    return string[::-1]
    pass


assert (inversa("pepito") == "otipep")

assert (inversa("luz") == "zul")

assert (inversa("z") == "z")

assert (inversa("") == "")


#Otra forma
def inversa1(cadena):
        return sorted(cadena, reverse = True)
        pass

