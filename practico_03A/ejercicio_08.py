# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

from practico_03_A.ejercicio_02 import agregar_persona
from practico_03_A.ejercicio_06 import reset_tabla
from practico_03_A.ejercicio_07 import agregar_peso
from practico_03_A.ejercicio_04 import buscar_persona
from practico_03_A.ejercicio_02 import session
from practico_03_A.ejercicio_06 import PersonaPeso


def listar_pesos(id_persona):
    pesos=[]
    if (buscar_persona(id_persona) == False):
        return False
    filtro=session.query(PersonaPeso).filter(PersonaPeso.idPersona==id_persona).all()
    for i in filtro:
        fp=(i.fecha,i.peso)
        pesos.append(fp)
    return pesos

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        (datetime.date(2018,5,1), 80),
        (datetime.date(2018,6,1), 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
