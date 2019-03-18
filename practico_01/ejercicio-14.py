# Programe un algoritmo recursivo que encuentre la salida de un laberinto,
# teniendo en cuenta que el laberinto se tomó como entrada y que es una matriz
# de valores True, False, (x,y) , donde True indica un obstáculo, False una celda
# donde se puede caminar, (x,y) es el punto donde comienza a buscarse la salida y
# (a,b), la salida del laberinto .

def resuelveLab( laberinto , entrada , salida ):
    # returns a list of the paths taken
    m, n = salida
    x , y = entrada
    if laberinto [m][n] is True:
        return print('La salida ingresada no es una salida valida para el laberinto.')
    elif laberinto[x][y] is True:
        return print('La entrada ingresada no tiene camino posible para recorrer.')
    else:
        if entrada == salida:
            return [salida]
        elif entrada ==( m - 1, n - 1 ):
            return [ ( m - 1 , n - 1 ) ]
        if x + 1 < len(laberinto) and laberinto[x + 1][y] is False:
            a = resuelveLab( laberinto , ( x + 1 , y ) , salida )
            if a != None:
                return [ (x , y ) ] + a
        if y + 1 < len(laberinto[0]) and laberinto[x][y + 1] is False:
            b = resuelveLab( laberinto , (x , y + 1) , salida )
            if  b != None:
                return [ ( x , y ) ] + b


laberinto = [[False, False, False, True],
             [False, True, True, True],
             [False, True, True, False],
             [False, False, True, True],
             [False, False, False, False]]

print (resuelveLab(laberinto,(0,0),(4,3)))
#Devuelve--> [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]

print (resuelveLab(laberinto,(2,0),(4,2)))
#Devuelve--> [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)]

print (resuelveLab(laberinto,(1,1),(4,2)))
#Devuelve--> La entrada ingresada no tiene camino posible para recorrer.

print (resuelveLab(laberinto,(0,0),(2,2)))
#Devuelve--> La salida ingresada no es una salida valida para el laberinto.
