from Datos.bebidas_datos import BebidaDatos
from negocio_mercadolibre.ComunicacionAPI import ComunicacionesAPI

class ErrorCantidad(Exception):
    pass

class NegocioBebida(object):

    def __init__(self):
        self.bebidas = BebidaDatos()
        self.comunicacionApi = ComunicacionesAPI()

    def get(self,cod):

        return self.bebidas.get(cod)

    def get_all(self):

        return self.bebidas.get_all()

    def get_all_tipo_bebida(self,tipo_bebida):

        return self.bebidas.get_all_tipo_bebida(tipo_bebida)

    def alta(self,bebida):

        return self.bebidas.alta(bebida)

    def baja(self,cod):
        try:
            self.bebidas.baja(cod)
            p = self.comunicacionApi.buscar_publicacion_por_sku(cod)
            if p:
                self.comunicacionApi.eliminar_por_codigo(cod)
        except Exception as e:
            return "Error al dar de baja el producto"
        return True


    def modificacion(self,bebida):
        try:
            self.bebidas.modificacion(bebida)
            p = self.comunicacionApi.buscar_publicacion_por_sku(bebida.id_bebida)
            if p:
                self.comunicacionApi.editar(bebida.id_bebida,bebida.precio,bebida.stock)
        except Exception as e:
            return " ha ocurrido un error, por favor verifique que datos se han modificado  ERROR : "+ str(e)
        return True

    def modificacion_ml(self):

        try:
            productos_ml = self.comunicacionApi.obtener_informacion_publicaciones()
            bebidas_modificadas = []
            for producto_ml in productos_ml:
                bebida = self.get(int(producto_ml[0]))
                if bebida != None:
                    if producto_ml[2] != bebida.stock and bebida != None:
                        bebida.titulo_bebida = producto_ml[1]
                        bebida.stock = producto_ml[2]
                        bebida.precio = producto_ml[4]
                        self.bebidas.modificacion(bebida)
                        bebidas_modificadas.append(bebida)
        except Exception as e:
            return str(e)

        return bebidas_modificadas

    def compra(self, id, cantidad):
        try:
            bebida = self.get(id)
            self.comparar_cantidades(bebida.stock,cantidad)
            bebida.stock = bebida.stock - cantidad
            self.modificacion(bebida)
        except ErrorCantidad as e:
            return e
        except Exception as e:
            return e
        else:
            return True

    def comparar_cantidades(self,stock,cantidad):

        if cantidad <= stock:
            print("Menor")
            return True
        else:
            print("Mayor")
            raise ErrorCantidad("No hay stock suficiente para esa cantidad pedida")
