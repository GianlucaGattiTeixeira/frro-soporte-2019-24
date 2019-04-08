# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

#from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
        carreras = []
        carreras_ordenadas = []
        diccionario = {}
        i = 0
        for x in range(len(estudiantes)):
                carreras.append(estudiantes[x])
        carreras_ordenadas = sorted(carreras)
        while(i < len(carreras_ordenadas)):
                cantidad = carreras_ordenadas.count(carreras_ordenadas[i])
                diccionario[carreras_ordenadas[i]] = cantidad
                i = i+ cantidad
        return diccionario

print("gol<")
print(organizar_estudiantes(["hola","hola","a","a"]))

