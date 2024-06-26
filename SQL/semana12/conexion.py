from cs50 import SQL

db = SQL("sqlite:///ejemplo.db")

# db.execute(''' CREATE TABLE IF NOT EXISTS Estudiante
# (
# id integer PRIMARY KEY,
# nombre varchar(30) NOT NULL,
# carrera varchar(50) NOT NULL

# )
# ''')

nombre = input("Ingrese el nombre del estudiante: ")
carrera = input("Ingrese la carrera que estudia: ")
db.execute('''
    INSERT INTO estudiante(nombre, carrera)
    VALUES(?, ?)

''', nombre, carrera)

dato = input("Inserte el nombre a buscar: ")
result = db.execute(''' SELECT * FROM estudiante WHERE nombre = ? ''', dato)[0]

print("{} está en la carrera {}".format(result["nombre"], result["carrera"]))