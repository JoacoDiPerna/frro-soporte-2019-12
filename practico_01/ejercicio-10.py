# Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.

# La función devolverá la primer palabra "más larga".
def mas_larga(lista):
    length = 0
    index = 0
    for i in range(0, len(lista)):
        if len(lista[i]) > length:
            length = len(lista[i])
            index = i
    return lista[i]
    pass


lista = ["caldo", "pepas", "manolo", "diaspora"]

assert (mas_larga(lista) == "diaspora")

assert (mas_larga(lista) != "manolo")


#Otra forma
def mas_larg(lista1):
    return sorted(lista1, key=len)
    pass

