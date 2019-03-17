# Programe un algoritmo recursivo que encuentre la salida de un laberinto,
# teniendo en cuenta que el laberinto se tomó como entrada y que es una matriz
# de valores True, False, (x,y) , donde True indica un obstáculo, False una celda
# donde se puede caminar, (x,y) es el punto donde comienza a buscarse la salida y
# (a,b), la salida del laberinto .


# Entendemos que no se está aplicando la recursividad como la consigna lo pide.
# Además el algoritmo sólo sigue un camino. Es decir, no vuelve atrás si se topa con un camino sin salida.
# Por ende sólo resuelve los laberintos que tienen un sólo camino válido.
recorrido = []


def buscar_salida(matriz, entrada, salida):
    global recorrido

    def buscar_siguiente_movimiento(matriz, x, y):
        ancho = len(matriz[0])
        alto = len(matriz)
        posicion = (x, y)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x + i, y + j) not in recorrido and x + i >= 0 and y + j >= 0 and x + i <= alto - 1 and \
                        y + j <= ancho - 1 and (x + i, y + j) != (x, y) and matriz[x + i][y + j] is True:
                    posicion = (x + i, y + j)
                    return posicion
        return posicion
        pass

    band = True
    actual = entrada

    if actual == salida:
        return band

    recorrido.append(entrada)
    x, y = entrada

    siguiente_movimiento = buscar_siguiente_movimiento(matriz, x, y)

    while band and siguiente_movimiento != salida:
        if siguiente_movimiento != actual:
            actual = siguiente_movimiento
            recorrido.append(actual)
            x, y = actual
            siguiente_movimiento = buscar_siguiente_movimiento(matriz, x, y)
        else:
            band = False
    return band

    pass


matriz = [[True, True, False],
          [False, True, False],
          [False, True, True],
          [False, False, True]]
entrada = (0, 0)
salida = (3, 2)
recorrido = []
assert (buscar_salida(matriz, entrada, salida) is True)

matriz = [[True, True, False],
          [False, False, False],
          [False, True, True],
          [False, False, False]]
entrada = (0, 0)
salida = (2, 2)
recorrido = []
assert (buscar_salida(matriz, entrada, salida) is False)
