# Crear una lista inicial
numeros = [1, 2, 3, 4, 5, "Hola", 5.6, True, [6,7]]
print("Lista inicial:", numeros[1:3])

# Utilizar el método append para añadir un elemento al final de la lista
numeros.append(6)
print("Lista después de append:", numeros)

#saber si un elemento pertenece a la lista
print(2 in numeros)

# Utilizar el método clear para eliminar todos los elementos de la lista
numeros.clear()
print("Lista después de clear:", numeros)

# Crear una nueva lista
colores = ["rojo", "verde", "azul"]
print("Lista de colores:", colores)

# Utilizar el método copy para obtener una copia de la lista
copia_colores = colores.copy()
print("Copia de la lista de colores:", copia_colores)

# Utilizar el método count para contar el número de veces que aparece un valor en la lista
cantidad_azul = colores.count("azul")
print("Cantidad de veces que aparece 'azul':", cantidad_azul)

# Utilizar el método extend para añadir los elementos de otra lista al final de la lista actual
otros_colores = ["amarillo", "rosa"]
colores.extend(otros_colores)
print("Lista extendida con otros colores:", colores)

# Utilizar el método index para obtener el índice del primer elemento con un valor específico
indice_rojo = colores.index("rojo")
print("Índice de 'rojo':", indice_rojo)

# Utilizar el método insert para añadir un elemento en una posición especificada
colores.insert(1, "morado")
print("Lista con 'morado' insertado en la posición 1:", colores)

# Utilizar el método pop para eliminar un elemento en una posición especificada y obtener su valor
valor_eliminado = colores.pop(2)
print("Valor eliminado en la posición 2:", valor_eliminado)
print("Lista después de pop:", colores)

# Utilizar el método remove para eliminar un elemento con un valor específico
colores.remove(colores[1])
print("Lista después de remove:", colores)

# Utilizar el método reverse para invertir el orden de los elementos de la lista
colores.reverse()
print("Lista después de reverse:", colores)

# Utilizar el método sort para ordenar los elementos de la lista
colores.sort()
print("Lista después de sort:", colores)


