from sqlalchemy import exc,create_engine
from sqlalchemy.orm import sessionmaker
from Datos.bebida import Bebida,Base


class BebidaDatos(Bebida):

    def __init__(self):
        self.db = create_engine('mysql://soporte2019:soporte2019@localhost:3306/vinos_mercado_libre')
        Base.metadata.bind = self.db
        db_session = sessionmaker()
        db_session.bind = self.db
        self.session = db_session()

    def get(self,codigo):

        try:
            bebida = self.session.query(Bebida).filter(Bebida.id_bebida == codigo).first()
        except exc.SQLAlchemyError:
            raise Exception("Error base de datos: ")
        else:
            return bebida

    def get_all(self):
        try:
            bebidas = self.session.query(Bebida).all()
        except exc.SQLAlchemyError:
            raise Exception("Error base de datos")
        else:
            return bebidas

    def get_all_tipo_bebida(self,tipo_bebida):
        try:
            bebidas = self.session.query(Bebida).filter(Bebida.tipo_bebida == tipo_bebida).all()
        except exc.SQLAlchemyError as e:
            raise Exception("Error base de datos")
        else:
            return bebidas

    def alta(self, bebida):
        try:
            self.session.add(bebida)
            self.session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            return str(e)
        else:
            return True

    def baja(self, cod):
        try:
            self.session.delete(self.session.query(Bebida).get(cod))
            self.session.commit()
        except exc.SQLAlchemyError as e:
            raise Exception("Error al dar de baja la bebida, "+e)

    def modificacion(self, bebida):
        try:
            x = self.session.query(Bebida).get(bebida.id_bebida)
            x.id_bebida = bebida.id_bebida
            x.titulo_bebida = bebida.titulo_bebida
            x.stock = int(bebida.stock)
            x.precio = float(bebida.precio)
            x.tipo_bebida = bebida.tipo_bebida
            self.session.commit()
        except Exception as e:
            raise Exception("Error al modificar una bebida ("+str(e)+")")
