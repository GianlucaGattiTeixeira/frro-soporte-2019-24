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

import random

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = ""
        self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        return False

    # llamarlo desde __init__
    def generar_dni(self):
        for i in range(8):
            self.dni = self.dni[:i] + str(random.randint(0,9))

    def print_data(self):
        print('Nombre: '+self.nombre+'\nEdad: '+str(self.edad)+'\nSexo: '+self.sexo+
            '\nPeso: '+str(self.peso)+'\nAltura: '+str(self.altura)+'\nDni: '+self.dni)


pers = Persona('Lucas',21,'H',80,176)
pers.print_data()
