# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String,Date
from sqlalchemy import create_engine

Base = declarative_base()

class Persona(Base):
    __tablename__='personas'
    idPersona=Column(Integer,primary_key=True)
    nombre=Column(String(30))
    fechaNacimiento=Column(Date)
    dni=Column(Integer)
    altura=Column(Integer)

def crear_tabla():
    Base.metadata.create_all(engine)

def borrar_tabla():

    Base.metadata.drop_all(bind=engine,tables=[Persona.__table__])

def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper



engine=create_engine('sqlite:///mibase2.db')
Base.metadata.bind = engine
