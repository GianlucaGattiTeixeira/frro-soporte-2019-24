# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import datetime
import sqlite3
from practico_03_A.ejercicio_01 import Persona, engine, Base
from practico_03_A.ejercicio_01 import borrar_tabla, crear_tabla
from sqlalchemy import Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship

class PersonaPeso(Base):
    __tablename__='personaPeso'
    idPersona=Column(Integer,ForeignKey('personas.idPersona'),primary_key=True)
    fecha=Column(Date,primary_key=True)
    peso=Column(Integer)
    personas = relationship(Persona)


def crear_tabla_peso():
    Base.metadata.create_all(engine) #si el engine lo importo creo la tabla del ejercicio 1 tambien?

def borrar_tabla_peso():
    Base.metadata.drop_all(bind=engine,tables=[PersonaPeso.__table__])

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper


crear_tabla_peso()
borrar_tabla_peso()
