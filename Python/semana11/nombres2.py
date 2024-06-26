import csv
estudiantes = []

while True:
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    nota = float(input("Ingrese la nota: "))

    estudiantes.append({"nombre" : nombre,
                        "apellido" : apellido,
                        "nota" : nota})
    opc = input("Desea ingresar otro nombre? (s/n)")
    if opc == "n":
        break
file = open("estudiantes.csv", "a")
writer = csv.writer(file)

for alumno in estudiantes:
    writer.writerow([alumno["nombre"], alumno["apellido"], alumno["nota"]])

    file.close()