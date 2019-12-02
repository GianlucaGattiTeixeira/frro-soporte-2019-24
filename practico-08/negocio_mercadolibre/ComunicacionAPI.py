#from codigo_viejo import Producto_Uploader_Vinos
from lib.meli import Meli
from athorization_info import info
from Datos.bebidas_datos import BebidaDatos, Bebida
import json

class ComunicacionesAPI:



    def realizar_publicacion(self, bebida):
        pro = bebida
        uploader = Producto_Uploader_Vinos(pro)
        cuerpo = uploader.toJson()
        meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                    access_token=info.access_token, refresh_token="")
        response = meli.post("/items", cuerpo, {"access_token": meli.access_token})
        return response.status_code



    def obtener_todas_publicaciones(self):
        meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                    access_token=info.access_token, refresh_token="")
        response = meli.get("/users/"+meli.client_id+"/items/search", params = {"access_token": meli.access_token, "status" : "active"})
        response_json = self.a_json(response)
        publicaciones = response_json.get("results")
        return publicaciones



    def obtener_informacion_publicaciones(self):
        listado_publicaciones = self.obtener_todas_publicaciones()
        meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                    access_token=info.access_token, refresh_token="")
        respuestas = []
        for i in listado_publicaciones:
            response = meli.get("/items/", params={"access_token": meli.access_token,"ids": i})
            response_json = self.a_json(response)
            respuestas.append([response_json[0].get("body").get("seller_custom_field"),
                               response_json[0].get("body").get("title"),
                               response_json[0].get("body").get("available_quantity"),
                               i,
                               response_json[0].get("body").get("price")])
        return respuestas   #devuelve lista con [codigoDelProductoEnLaDB,
                            #titulo, cantidadDisponible, CodigoPublicacionEnMercadolibre]


    def obtener_id_publicados(self):
        info = self.obtener_informacion_publicaciones()
        ids = []
        for i in info:
            ids.append(i[0])
        return ids



    def a_json(self,bytearray):
        string = bytearray.content.decode("utf-8")
        el_json = json.loads(string)
        return el_json



    def eliminar_publicacion(self,idsMercadolibre):
        exitosas = []
        fallidas = []
        meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                    access_token=info.access_token, refresh_token="")
        for i in idsMercadolibre:
            response = meli.put("/items/"+i,body = {"status":"closed"},
                                params = {"access_token": meli.access_token}) # SE DEBE VALIDAR QUE SE ELIMINEN

            if response.status_code != 200:
                fallidas.append(i)             #VERIFICAR SI AGREGA CUANDO ENTRA
            else:
                exitosas.append(i)
        return exitosas,fallidas



    def eliminar_por_codigo(self,idEnDB):
        #curl -X GET https://api.mercadolibre.com/users/$USER_ID/items/search?seller_sku=$SELLER_SKU&access_token=$ACCESS_TOKEN
        meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                    access_token=info.access_token, refresh_token="")
        #response = meli.get("/users/"+meli.client_id+"/items/search", params={"access_token": meli.access_token,"sku": idEnDB})      #SE DEBE VALIDAR QUE EXISTAN
        #response_json = self.a_json(response)
        result = self.buscar_publicacion_por_sku(idEnDB)
        if not result:
            raise Exception("no existe publicacion para dicho id")
        else:
            exitosas, fallidas = self.eliminar_publicacion(result)
            return exitosas,fallidas




    def buscar_publicacion_por_sku(self,idEnDB):
        try:
            meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                        access_token=info.access_token, refresh_token="")
            response = meli.get("/users/"+meli.client_id+"/items/search",
                                params={"access_token": meli.access_token,"sku": str(idEnDB),  "status" : "active"})
            response_json = self.a_json(response)
            result = response_json.get("results")
            return result
        except Exception as e:
            srtError = str(e)
            raise (str(e))


    def editar_precio(self, codigo , nuevo_precio ):                                                  #CHEQUEAR
        fallidos = []
        exitosos = []
        publicaciones = self.buscar_publicacion_por_sku(codigo)
        meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                    access_token=info.access_token, refresh_token="")
        if not publicaciones:
            raise Exception( "el producto de codigo {} no ha sido publicado".format(codigo) )
        else:
            for i in publicaciones:
                response = meli.put("/items/"+i,body = {"price":str(nuevo_precio)},
                                    params = {"access_token": meli.access_token})
                if response.status_code != 200:
                    fallidos.append(i)
                else:
                    exitosos.append(i)
            return exitosos, fallidos


    def editar(self, codigo , nuevo_precio, nuevo_stock ):                                                  #CHEQUEAR
        fallidos = []
        exitosos = []
        publicaciones = self.buscar_publicacion_por_sku(codigo)
        meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                    access_token=info.access_token, refresh_token="")
        if not publicaciones:
            raise Exception( "el producto de codigo {} no ha sido publicado".format(codigo) )
        else:
            for i in publicaciones:
                response = meli.put("/items/"+i,body = {"price":str(nuevo_precio),"available_quantity":str(nuevo_stock)},
                                    params = {"access_token": meli.access_token})
                if response.status_code != 200:
                    fallidos.append(i)
                else:
                    exitosos.append(i)
            return exitosos, fallidos

    def editar_cantidad(self):
        pass

    def editar_titulo(self):
        pass


    def actualizae_stock(self):
        pass


    def listar_todos_los_publicados(self):
        try:
            bebidas_publicadas = []
            ids_pub = self.obtener_id_publicados()
            b = BebidaDatos()
            meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                        access_token=info.access_token, refresh_token="")
            vistos = []
            for i in ids_pub:
                if str(i) not in (vistos):
                    vistos.append(i)
                    bebida = b.get(i)
                    if bebida != None:
                        bebidas_publicadas.append(bebida)
                    else:
                        self.eliminar_por_codigo(i)                               #revisar esto

            return bebidas_publicadas
        except Exception as e:
            raise Exception( "Ocurrió un error a la hora de listar los productos, "
                             "  ERROR:  " + str(e))



    def listar_todos_no_publicados(self):
        try:
            bebidasNoPublicadas = []
            ids_pub = self.obtener_id_publicados()
            b = BebidaDatos()
            bebidas = b.get_all()
            meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                        access_token=info.access_token, refresh_token="")
            for i in bebidas:
                if str(i.id_bebida) not in (ids_pub):
                    bebidasNoPublicadas.append(i)
            return bebidasNoPublicadas
        except Exception as e:
            raise Exception( "Ocurrió un error a la hora de listar los productos, "
                             "  ERROR:  " + str(e))




    def publicar_todos_no_publicados(self):
        try:
            exitosos = []
            fallidos = []
            ids_pub = self.obtener_id_publicados()
            b = BebidaDatos()
            bebidas = b.get_all()
            meli = Meli(client_id=info.client_id, client_secret=info.client_secret,
                        access_token=info.access_token, refresh_token="")
            for i in bebidas:
                if str(i.id_bebida) not in (ids_pub):
                    status_code = self.realizar_publicacion(i)
                    if str(status_code) != "201":
                        fallidos.append(i)
                    else:
                        exitosos.append(i)
            return exitosos , fallidos
        except Exception as e:
            raise Exception( "Ocurrió un error a la hora de publicar los productos, "
                            "por favor chequee la pagina de productos no publicados para conocer "
                            "si restan productos por publicar" "   ERROR:  " + str(e))




class Producto_Uploader_Vinos():
    def __init__(self,bebida):
        self.seller_custom_field = bebida.id_bebida
        self.title = bebida.titulo_bebida
        self.available_quantity = bebida.stock
        self.price = bebida.precio
        self.pictures=[{"source":"http://mla-s2-p.mlstatic.com/968521-MLA20805195516_072016-O.jpg"}]
        self.category_id ="MLA3530" #"MLA1403"
        self.currency_id = "ARS"
        self.buying_mode ="buy_it_now"
        self.listing_type_id = "gold_pro"
        self.description = "Item de test - No Ofertar"
        self.attributes = [{ "id" : "ITEM_CONDITION", "value_id": "2230582"}]
        self.sale_terms = [{"id": "WARRANTY_TYPE", "value_id": "2230279" },
                           {"id": "WARRANTY_TIME", "value_name": "90 dias"}]


    def toJson(self):
        body ={
                "title" : self.title,
                "category_id" : self.category_id,
                "price" : self.price,
                "currency_id" : self.currency_id,
                "available_quantity" : self.available_quantity,
                "buying_mode" : self.buying_mode,
                "listing_type_id" : self.listing_type_id,
                "description" : self.description,
                "attributes" : self.attributes,
                "sale_terms" : self.sale_terms,
                "pictures" : self.pictures,
                "seller_custom_field": str(self.seller_custom_field)
                }
        return body

if __name__ == "__main__":
    s = ComunicacionesAPI()
    #s.publicar_todos()
    #b1 = Bebida(1, "rutini reserva 2015", 8, 900)
    #b2 = Bebida(2, "Amalaya dulce natural", 9, 300)
    #s.realizar_publicacion(b1)
    #s.realizar_publicacion(b2)
    #s.publicar_todos()
    #ids = s.obtener_id_publicados()
    #elim = s.eliminar_por_codigo(1)
    #print(elim)
    #publicaciones = s.listar_todos_no_publicados()
    #for i in publicaciones:
    #    print(i.id_bebida, " ", i.titulo_bebida )
    #e,f = s.editar_precio(1, 668)
    #print("exitosos   ", e, "fallidos  ", f)
    #r = s.eliminar_por_codigo(13)
    #s.editar( 16 , 50, 112 )
    print(s.listar_todos_no_publicados())
