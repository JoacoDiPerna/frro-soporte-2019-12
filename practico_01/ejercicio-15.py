# A) Reescriba el programa que pide al usuario una lista de números e imprime en pantalla el máximo y mínimo de los
# números introducidos al final, cuando el usuario introduce “fin”.
# B) Escriba ahora el programa de modo que almacene los números que el usuario introduzca en una lista y usa las
# funciones max () y min () para calcular los números máximo y mínimo después de que el bucletermine.


def busca_max_min():
    lista = []
    valores = input("Ingresar valor ('fin' para finalizar):")
    while valores.lower()!='fin':
        lista.append(valores)
        valores = input("Ingresar valor ('fin' para finalizar):")
    lista.sort()
    min = lista[0]
    lista.reverse()
    max = lista[0]
    print("El valor maximo es el numero:",max)
    print("El valor minimo es el numero:",min)
    pass

#Probar por consola
busca_max_min()
