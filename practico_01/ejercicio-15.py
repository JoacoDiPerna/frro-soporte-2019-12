# A) Reescriba el programa que pide al usuario una lista de números e imprime en pantalla el máximo y mínimo de los
# números introducidos al final, cuando el usuario introduce “fin”.
# B) Escriba ahora el programa de modo que almacene los números que el usuario introduzca en una lista y usa las
# funciones max () y min () para calcular los números máximo y mínimo después de que el bucletermine.

#Apartado A)
def buscaValores():
    max = min = 0
    nro=input("Ingresar valor ('fin' para finalizar):")
    while nro != 'fin':
        if max == 0 and min == 0:
            max = min = int(nro)
        if int(nro) > max:
            max = int(nro)
        if int(nro) < min:
            min = int(nro)
        nro=input("Ingresar valor ('fin' para finalizar):")
    print("El valor minimo es el numero: %s" %min)
    print("El valor maximo es el numero: %s" %max)

#Probar por consola.
buscaValores()


#Apartado B)
def busca_max_min():
    lista = []
    valores = input("Ingresar valor ('fin' para finalizar):")
    while valores.lower() != 'fin':
        lista.append(int(valores))
        valores = input("Ingresar valor ('fin' para finalizar):")
    print("El valor minimo es el numero: %s" %min(lista))
    print("El valor maximo es el numero: %s" %max(lista))
    pass

# Probar por consola.
busca_max_min()

