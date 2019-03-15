# Definir una funciÃ³n max() que tome como argumento dos nÃºmeros y devuelva el mayor de ellos.


def max(a, b):
    if a < b:
        return b
    else:
        return a
    pass


assert (max(1, 5) == 5)

assert (max(10, 4) == 10)

assert (max(4, 4) == 4)
