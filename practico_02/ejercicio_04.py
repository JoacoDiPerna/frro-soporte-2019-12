# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

from practico_02.ejercicio_03 import Persona
from datetime import datetime


class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super(Estudiante, self).__init__(nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        return self.cantidad_aprobadas / self.cantidad_materias

    # implementar usando modulo datetime
    def edad_ingreso(self):
        return self.edad - (datetime.now().year - self.anio)


estudiante = Estudiante("Pedro Rodiguez", 24, "H", 75, 1.77, "ISI", 2012, 42, 34)
estudiante.print_data()
assert (estudiante.avance() == 0.8095238095238095)
assert (estudiante.edad_ingreso() == 17)
