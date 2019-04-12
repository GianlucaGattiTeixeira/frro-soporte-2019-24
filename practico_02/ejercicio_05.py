# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
        carreras = []
        carreras_ordenadas = []
        diccionario = {}
        i = 0
        for x in range(len(estudiantes)):
                carreras.append(estudiantes[x].carrera)
        carreras_ordenadas = sorted(carreras)
        while(i < len(carreras_ordenadas)):
                cantidad = carreras_ordenadas.count(carreras_ordenadas[i])
                diccionario[carreras_ordenadas[i]] = cantidad
                i = i + cantidad
        return diccionario

estudiantes = []
e1 = Estudiante('Pedro',20,'M',120,50,'Contabilidad',2000,20,10)
e2 = Estudiante('Pedro',20,'M',120,50,'Psicologia',2000,20,10)
e3 = Estudiante('Pedro',20,'M',120,50,'Ingenieria',2000,20,10)
e4 = Estudiante('Pedro',20,'M',120,50,'Contabilidad',2000,20,10)
e5 = Estudiante('Pedro',20,'M',120,50,'Ingenieria',2000,20,10)
estudiantes.append(e1)
estudiantes.append(e2)
estudiantes.append(e3)
estudiantes.append(e4)
estudiantes.append(e5)

dic = organizar_estudiantes(estudiantes)
assert dic['Contabilidad'] == 2
assert dic['Ingenieria'] == 2
assert dic['Psicologia'] == 1


