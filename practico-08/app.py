from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from negocio_mercadolibre import ComunicacionAPI
from Negocio.bebidas import NegocioBebida
from Datos.bebida import Bebida
from Datos.bebidas_datos import BebidaDatos

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)

def get_datos(bebidas):
    imagenes = []
    for bebida in bebidas:
        if bebida.imagen:
            imagenes.append(str(bebida.imagen).split("'")[1])

    datos = [bebidas,imagenes]
    return datos


@app.route('/')
def default():

    return redirect(url_for("admin_bebidas",tipo_bebida="vino"))

@app.route('/<string:tipo_bebida>',methods=["GET","POST"])
def get_bebidas(tipo_bebida):

    bebidas = negocio_bebida.get_all_tipo_bebida(tipo_bebida)

    datos = get_datos(bebidas)
    rango = range(len(datos[0]))

    return render_template("index.html",datos=datos,rango=rango)

@app.route('/compra',methods=["GET","POST"])
def compra():
    if request.method == "POST":
        try:
            cantidad = request.form["cantidad"]
            id = request.form["id"]
            bebida = negocio_bebida.get(id)
            validacion(cantidad)
            salida = negocio_bebida.compra(id,int(cantidad))
            print(salida)
            if salida is True:

                flash("La compra ha sido exitosa")
                return render_template("informar_compra.html",bebida=bebida,cantidad=cantidad)
            else:
                flash(salida,"fail")
                return get_bebidas(bebida.tipo_bebida)
        except ErrorTipoDato as e:
            flash(e,"fail")
            return get_bebidas(bebida.tipo_bebida)

@app.route('/admin')
def admin():

    return redirect(url_for("admin_bebidas",tipo_bebida="vino"))

@app.route('/admin/<string:tipo_bebida>')
def admin_bebidas(tipo_bebida='vino'):

    vinos = negocio_bebida.get_all_tipo_bebida(tipo_bebida)

    datos = get_datos(vinos)
    rango = range(len(datos[0]))

    return render_template("listadoDeProductosLocales.html",datos=datos,rango=rango)

@app.route( '/admin/editar_producto' , methods = ["GET","POST"] )
def editar_producto():

    if request.method == "POST":
        try:
            id = request.form["id"]
            bebida = negocio_bebida.get(id)
            stock = request.form['stock']
            precio = request.form['precio']
            validaciones(precio,stock)

            bebida.stock = stock
            bebida.precio = precio

            salida =negocio_bebida.modificacion(bebida)

            if salida:
                flash("El producto se ha modificado correctamente")
                return render_template("informar.html",bebida=bebida)

            return render_template("error.html",error=str(salida))
        except ErrorTipoDato as e:
            flash(e,"fail")
            return render_template("editar.html",datos=bebida)

    id = request.args.get("id")
    bebida = negocio_bebida.get(id)
    return render_template("editar.html",datos=bebida)

@app.route('/admin/alta',methods=["Get","post"])
def alta_producto():

    if request.method == "POST":
        try:
            precio = request.form['precio']
            stock = request.form['stock']
            validaciones(precio,stock)

            nombre = request.form['nombre']
            tipo = request.form['tipo']
            bebida = Bebida(titulo_bebida=nombre,stock=stock,precio=precio,imagen=None,tipo_bebida=tipo)

            salida = negocio_bebida.alta(bebida)
            if salida:
                flash("El producto se ha dado de alta correctamente")
                return render_template("informar.html",bebida=bebida)
            else:
                return render_template("error.html",error = salida)
        except ErrorTipoDato as e:
            flash(e,"fail")
            return render_template("alta.html")

    return render_template("alta.html")

class ErrorTipoDato(Exception):
    pass

def validaciones(precio,stock):

    try:
        float(precio)
        int(stock)
        return True
    except Exception:
        raise ErrorTipoDato("Los valores de precios y stock deben ser numéricos")

def validacion(cant):

    try:
        int(cant)
        return True
    except Exception:
        print("Error tipo dato")
        raise ErrorTipoDato("La cantidad debe ser un valor numérico")

@app.route("/admin/eliminar",methods=["GET","POST"])
def eliminar_producto():

    if request.method == "POST":
        id = request.form['id']
        bebida = negocio_bebida.get(id)
        salida = negocio_bebida.baja(id)

        if salida:
            flash("El producto se ha eliminado correctamente")
            return render_template("informar.html",bebida=bebida)

        return render_template("error.html",error = str(salida))


@app.route("/admin/listar_productos_no_subidos")
def listarProductosNoSubidos():
    try:
        c = ComunicacionAPI.ComunicacionesAPI()
        bebidas = c.listar_todos_no_publicados()
        return render_template("listar_productos_no_subidos.html", bebidas = bebidas)
    except Exception as e:
        texto = str(e)
        return render_template("error.html" , error = texto)


@app.route("/admin/publicar_todos_no_publicados")
def publicarProductosNoSubidos():
    try:
        c = ComunicacionAPI.ComunicacionesAPI()
        exitosos, fallidos =c.publicar_todos_no_publicados()
        return render_template("resultados_publicar_todos_los_no_publicados.html",
                               exitosos = exitosos, fallidos = fallidos)
    except Exception as e:
        texto = str(e)
        return render_template("error.html" , error = texto)



@app.route("/admin/mostrar_informacion_del_producto_a_subir/<id>")
def mostrar_informacion_del_producto_a_subir(id):
    try:
        c = ComunicacionAPI.ComunicacionesAPI()
        p = c.buscar_publicacion_por_sku(id)
        if not p:
            d = BebidaDatos()
            bebida = d.get(id)
            return render_template("mostrar_informacion_de_producto_a_subir.html", bebida = bebida)
        else:
            return render_template("error.html", error = "el producto ya ha sido subido a Mercado Libre")
    except Exception as e:
        texto = "Ocurrio un error  "  + str(e)
        return render_template("error.html" , error = texto)


@app.route("/admin/publicar_producto/<int:id>")
def publicar_producto(id):
    c = ComunicacionAPI.ComunicacionesAPI()
    bebida = negocio_bebida.get(id)
    status = c.realizar_publicacion(bebida)
    #stringGenerado = str(id)+ " status de subida " + str(status)
    if str(status) == '201':
        flash('Producto subido exitosamente a Mercado Libre')
        return render_template("resultado_publicar_un_producto.html",bebida=bebida)
    else:
        return render_template("error.html",error=str(status))

@app.route("/admin/actualizar")
def actualizar():

    bebidas_mod = negocio_bebida.modificacion_ml()
    if type(bebidas_mod) != str:
        return render_template("listado_de_productos_stock_act_ML.html", bebidas = bebidas_mod)
    else:
        return render_template("error.html", error = bebidas_mod)


if __name__ == "__main__":
    negocio_bebida = NegocioBebida()
    app.run(port=5391)
