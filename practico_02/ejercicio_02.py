# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

from math import pi


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2

    def perimetro(self):
        return 2 * pi * self.radio


circulo = Circulo(4)
assert circulo.area() == 50.26548245743669
assert circulo.perimetro() == 25.132741228718345
