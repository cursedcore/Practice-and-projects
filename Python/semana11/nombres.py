from cs50 import get_string, get_int
estudiantes = {"nombre": "",
               "apellido" : "",
               "nota" : 0}
lista = []
n = get_int("Ingrese la cantidad de estudiantes: ")
for i in range(n):
    nombre = get_string("Escriba el nombre del estudiante #%d: " %(i+1))
    lista.append(nombre)
    estudiantes['nombre'] = lista
    apellido = get_string("Escriba el apellido del estudiante #%d: " %(i+1))
    lista.append(apellido)
    estudiantes['apellido'] = lista
    nota = get_int("Escriba la nota del estudiante #%d: " %(i+1))
    lista.append(nota)
    estudiantes['nota'] = lista
print()
for i in lista:
    print(i)



