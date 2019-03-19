# Programe un algoritmo recursivo que encuentre la salida de un laberinto,
# teniendo en cuenta que el laberinto se tomó como entrada y que es una matriz
# de valores True, False, (x,y), donde True indica un obstáculo, False una celda
# donde se puede caminar, (x,y) es el punto donde comienza a buscarse la salida y
# (a,b), la salida del laberinto.


def resuelveLab(laberinto, entrada, salida):
    x, y = entrada
    a, b = salida

    alto = len(laberinto)
    ancho = len(laberinto[0])

    if x >= alto or a >= alto or y >= ancho or b >= ancho or x < 0 or a < 0 or y < 0 or b < 0:
        return print('Se sobrepasan los límites del laberinto.')
    elif laberinto[a][b] is True:
        return print('La salida ingresada no es una salida valida para el laberinto.')
    elif laberinto[x][y] is True:
        return print('La entrada ingresada no pertenece al camino de salida del laberinto.')

    else:
        if entrada == salida:
            return [salida]

        if (x - a) <= 0:
            if x + 1 < alto and laberinto[x + 1][y] is False:
                a = resuelveLab(laberinto, (x + 1, y), salida)
                if a is not None:
                    return [(x, y)] + a
                else:
                    return print('No existe camino posible.')
        else:
            if x - 1 < alto and laberinto[x - 1][y] is False:
                b = resuelveLab(laberinto, (x - 1, y), salida)
                if b is not None:
                    return [(x, y)] + b
                else:
                    return print('No existe camino posible.')

        if (y - b) <= 0:
            if y + 1 < ancho and laberinto[x][y + 1] is False:
                c = resuelveLab(laberinto, (x, y + 1), salida)
                if c is not None:
                    return [(x, y)] + c
                else:
                    return print('No existe camino posible.')
        else:
            if y - 1 < ancho and laberinto[x][y - 1] is False:
                d = resuelveLab(laberinto, (x, y - 1), salida)
                if d is not None:
                    return [(x, y)] + d
                else:
                    return print('No existe camino posible.')
    pass


laberinto = [[False, False, False, True],
             [False, True, True, True],
             [False, False, True, False],
             [True, False, True, True],
             [False, False, False, False]]

print(resuelveLab(laberinto, (0, 0), (4, 3)))
# Devuelve--> [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3)]

print(resuelveLab(laberinto, (2, 0), (4, 1)))
# Devuelve--> [(2, 0), (2, 1), (3, 1), (4, 1)]

print(resuelveLab(laberinto, (4, 3), (0, 0)))
# Devuelve--> [(4, 3), (4, 2), (4, 1), (3, 1), (2, 1), (2, 0), (1, 0), (0, 0)]

print(resuelveLab(laberinto, (1, 1), (4, 2)))
# Devuelve--> La entrada ingresada no pertenece al camino de salida del laberinto. [None]

print(resuelveLab(laberinto, (1, 0), (3, 3)))
# Devuelve--> La salida ingresada no es una salida valida para el laberinto. [None]

print(resuelveLab(laberinto, (0, 1), (2, 3)))
# Devuelve--> No existe camino posible. [None]

print(resuelveLab(laberinto, (0, 1), (5, 3)))
# Devuelve--> Se sobrepasan los límites del laberinto. [None]
