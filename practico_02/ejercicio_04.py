# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual)
from ejercicio_03 import Persona
from datetime import date
class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura,carrera, anio, cantidad_materias, cantidad_aprobadas):
        super().__init__(nombre,edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        avance = self.cantidad_aprobadas/self.cantidad_materias
        return avance

    # implementar usando modulo datetime
    def edad_ingreso(self):
        edad_ingreso =self.edad-(date.today().year-self.anio)
        return edad_ingreso

e = Estudiante('Lucas',21,'H',80,176,'isi',2015,20,15)

assert e.avance()==0.75
assert e.edad_ingreso()==17