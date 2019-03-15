# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas).
# ejemplo: es_palindromo ("radar") tendría que devolver True.


# La función no distingue entre mayúsculas y minúsculas.
def es_palindromo(string):
    return string.lower() == string[::-1].lower()
    pass


assert (es_palindromo("Menem") is True)

assert (es_palindromo("Neuquen") is True)

assert (es_palindromo("falso") is False)
