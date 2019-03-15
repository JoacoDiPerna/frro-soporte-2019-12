# Programe una función que determine si un número entero suministrado como argumento es primo.


def es_primo(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            elif i == num - 1:
                return True
    pass


assert (es_primo(0) is False)

assert (es_primo(2) is True)

assert (es_primo(3) is True)

assert (es_primo(4) is False)

assert (es_primo(101) is True)