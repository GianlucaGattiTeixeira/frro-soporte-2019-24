# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import *
class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.fecha_nacimiento = datetime.strptime(nacimiento,'%d/%m/%Y')


    def edad(self):
        fecha_actual = datetime.now()
        año_actual = fecha_actual.year
        mes_actual = fecha_actual.month
        dia_actual = fecha_actual.day

        edad = año_actual - self.fecha_nacimiento.year
        if(self.fecha_nacimiento.month > mes_actual):
            edad = edad - 1
        elif(self.fecha_nacimiento.month == mes_actual):
            if(self.fecha_nacimiento.day > dia_actual):
                edad = edad - 1
        return edad

persona = Persona('01/01/2000')

assert persona.edad() == 19

