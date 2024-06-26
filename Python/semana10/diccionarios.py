pizzas = {
    "queso" : 9,
    "pepperoni" : 10,
    "vegetales" : 11,
    "pollo barbacoa": 12     }
for ing, precio in pizzas.items():
    print(f"Una pizza de {ing} cuesta ${precio}")
print("\n")

alumno = {
    "nombre" : "Juana",
    "edad" : 21,
    "nota promedio" : 8.6,
    "notas" : [90,80, 70],
    "materias": {
        "materia1" : "cálculo",
        "materia2" : "programación",
        "materia3" : "física"
    }
}
print(f"""El alumno {alumno['nombre']} con la edad de {alumno['edad']} consiguió un promedio de {alumno['nota promedio']}%\n""")
print(f"La primera nota de {alumno['nombre']} es: {alumno['notas'][0]}\n")
print(f"La nota de {alumno['materias']['materia1']} fue {alumno['notas'][2]}")



