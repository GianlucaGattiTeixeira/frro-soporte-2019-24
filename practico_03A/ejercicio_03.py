# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from practico_03_A.ejercicio_01 import reset_tabla
from practico_03_A.ejercicio_02 import agregar_persona
from practico_03_A.ejercicio_01 import Persona
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy import create_engine

def borrar_persona(id_persona):
    x = session.query(Persona).get(id_persona)
    if x is None:
        return False
    else:
        session.delete(x)
        session.commit()
        return True


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

engine=create_engine('sqlite:///mibase2.db')

DBSession=sessionmaker()
DBSession.bind=engine
session=DBSession()

if __name__ == '__main__':
    pruebas()
