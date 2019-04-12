# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
from math import pi

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = (pi*self.radio)**2
        return area

    def perimetro(self):
        perimetro = 2*pi*self.radio
        return perimetro


circ = Circulo(5)

assert circ.area() == (5**2)*(pi**2)
assert circ.perimetro() == 10*pi