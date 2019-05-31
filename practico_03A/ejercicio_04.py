# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from practico_03_A.ejercicio_01 import reset_tabla
from practico_03_A.ejercicio_02 import agregar_persona
from practico_03_A.ejercicio_01 import Persona
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy import create_engine

def buscar_persona(id_persona):
    x = session.query(Persona).filter(Persona.idPersona == id_persona).first()
    if x is None:
        return False
    else:
        tupla = (x.idPersona,x.nombre,x.fechaNacimiento,x.dni,x.altura)
        print(tupla)
        return tupla


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

engine=create_engine('sqlite:///mibase2.db')

DBSession=sessionmaker()
DBSession.bind=engine
session=DBSession()

if __name__ == '__main__':
    pruebas()
