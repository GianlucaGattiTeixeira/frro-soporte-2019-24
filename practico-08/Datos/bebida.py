from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Float,BLOB

Base = declarative_base()
class Bebida(Base):

    __tablename__ = 'bebidas'

    id_bebida = Column(Integer,primary_key=True)
    titulo_bebida = Column(String(50))
    stock = Column(Integer())
    precio = Column(Float)
    imagen = Column(BLOB)
    tipo_bebida = Column(String(45))
