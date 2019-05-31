# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
from practico_03_A.ejercicio_01 import reset_tabla
from practico_03_A.ejercicio_02 import agregar_persona
from practico_03_A.ejercicio_04 import buscar_persona
from practico_03_A.ejercicio_01 import Persona
from practico_03_A.ejercicio_02 import session

def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    x = session.query(Persona).filter(Persona.idPersona == id_persona).first()
    if x is None:
        return False
    x.nombre=nombre
    x.altura=altura
    x.dni=dni
    x.fechaNacimiento=nacimiento
    session.commit()
    return True


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.date(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
