# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

from practico_03_A.ejercicio_01 import Persona
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import datetime
from practico_03_A.ejercicio_01 import reset_tabla

def agregar_persona(nombre, nacimiento, dni, altura):
    operador=Persona()
    operador.nombre=nombre
    operador.altura=altura
    operador.dni=dni
    operador.fechaNacimiento=nacimiento
    session.add(operador)
    session.commit()
    lp=session.query(Persona).all()
    id=lp[len(lp)-1].idPersona
    return id

engine=create_engine('sqlite:///mibase2.db')

DBSession=sessionmaker()
DBSession.bind=engine
session=DBSession()

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
