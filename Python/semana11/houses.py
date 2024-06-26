import csv

casas = {
    "Gryffindor" : 0,
    "Hufflepuff" : 0,
    "Ravenclaw" : 0,
    "Slytherin" : 0}

with open("hogwarts.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for fila in reader:
        casas[fila[1]] += 1

for casa in casas:
    print(f'{casa} : {casas[casa]}')