# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
    dict = {'ISI': 0, 'IC': 0, 'IQ': 0}
    for e in estudiantes:
        if e.carrera in dict:
            dict[e.carrera] += 1

    return dict


l = []
estudiante = Estudiante("Pedro Rodiguez", 24, "H", 75, 1.77, "ISI", 2012, 42, 34)
l.append(estudiante)
estudiante = Estudiante("Jorgue Lopez", 28, "H", 65, 1.65, "IC", 2015, 42, 20)
l.append(estudiante)
estudiante = Estudiante("Margarita Flores", 22, "M", 80, 1.80, "ISI", 2017, 42, 10)
l.append(estudiante)

assert (organizar_estudiantes(l) == {'ISI': 2, 'IC': 1, 'IQ': 0})
