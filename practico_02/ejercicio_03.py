# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.

from random import randrange


class Persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        return randrange(00000000, 99999999)

    def print_data(self):
        print("Nombre: %s " % self.nombre)
        print("Apellido: %i " % self.edad)
        print("Sexo: %s " % self.sexo)
        print("Peso: %.1f " % self.peso)
        print("Altura: %.2f " % self.altura)
        print("Dni: %i " % self.dni)


persona = Persona("Pedro Rodiguez", 24, "H", 75, 1.77)
# persona.print_data()
assert (persona.es_mayor_edad() is True)

print("\n")

persona = Persona("Luisa Lopez", 17, "M", 60, 1.65)
# persona.print_data()
assert (persona.es_mayor_edad() is False)
