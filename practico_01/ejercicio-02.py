# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.


def max_de_tres(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c
    pass


assert (max_de_tres(3, 4, 6) == 6)

assert (max_de_tres(3, 10, 6) == 10)

assert (max_de_tres(37, 4, 6) == 37)

assert (max_de_tres(3, 3, 3) == 3)
