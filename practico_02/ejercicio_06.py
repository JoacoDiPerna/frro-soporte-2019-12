# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import datetime


class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        return ((datetime.now() - self.nacimiento) / (365.25)).days


persona1 = Persona(datetime(1994, 4, 18))

assert (persona1.edad() == 24)

persona1 = Persona(datetime(1994, 2, 10))

assert (persona1.edad() == 25)
