# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base * self.altura
        return area


rect = Rectangulo(3,3)
assert rect.area() == 9
