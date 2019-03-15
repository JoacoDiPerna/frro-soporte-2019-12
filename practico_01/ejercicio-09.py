# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx”


def generar_n_caracteres(n, char):
    return char * n
    pass


assert (generar_n_caracteres(5, "x") == "xxxxx")

assert (generar_n_caracteres(3, "z") == "zzz")

assert (generar_n_caracteres(8, "a") != "asdfs")
