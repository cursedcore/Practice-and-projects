# Crear conjuntos iniciales
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Conjunto 1:", set1)
print("Conjunto 2:", set2)

# Utilizar el método add para añadir un elemento al conjunto
set1.add(5)
print("Conjunto 1 después de add:", set1)

# Utilizar el método clear para eliminar todos los elementos del conjunto
set1.clear()
print("Conjunto 1 después de clear:", set1)

# Crear conjuntos nuevos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Conjunto 1:", set1)
print("Conjunto 2:", set2)

# Utilizar el método copy para obtener una copia del conjunto
set3 = set1.copy()
print("Copia del conjunto 1:", set3)

# Utilizar el método difference para obtener la diferencia entre dos conjuntos
difference = set1.difference(set2)
print("Diferencia entre conjunto 1 y conjunto 2:", difference)

# Utilizar el método difference_update para eliminar los elementos de un conjunto que están incluidos en otro conjunto
set1.difference_update(set2)
print("Conjunto 1 después de difference_update:", set1)

# Utilizar el método discard para eliminar un elemento especificado
set2.discard(4)
print("Conjunto 2 después de discard:", set2)

# Utilizar el método intersection para obtener la intersección entre dos conjuntos
intersection = set1.intersection(set2)
print("Intersección entre conjunto 1 y conjunto 2:", intersection)

# Utilizar el método intersection_update para eliminar los elementos de un conjunto que no están incluidos en otros conjuntos
set1.intersection_update(set2)
print("Conjunto 1 después de intersection_update:", set1)

# Utilizar el método isdisjoint para verificar si dos conjuntos tienen intersección o no
is_disjoint = set1.isdisjoint(set2)
print("¿Conjunto 1 y conjunto 2 son disjuntos?", is_disjoint)

# Utilizar el método issubset para verificar si otro conjunto contiene al conjunto o no
is_subset = set1.issubset(set2)
print("¿Conjunto 1 es subconjunto de conjunto 2?", is_subset)

# Utilizar el método issuperset para verificar si el conjunto contiene a otro conjunto o no
is_superset = set1.issuperset(set2)
print("¿Conjunto 1 es superconjunto de conjunto 2?", is_superset)

# Utilizar el método pop para eliminar un elemento del conjunto
elemento_eliminado = set1.pop()
print("Elemento eliminado con pop:", elemento_eliminado)
print("Conjunto 1 después de pop:", set1)

# Utilizar el método remove para eliminar un elemento especificado
set2.remove(5)
print("Conjunto 2 después de remove:", set2)

# Utilizar el método symmetric_difference para obtener la diferencia simétrica de dos conjuntos
symmetric_difference = set1.symmetric_difference(set2)
print("Diferencia simétrica entre conjunto 1 y conjunto 2:", symmetric_difference)

# Utilizar el método symmetric_difference_update para insertar la diferencia simétrica de un conjunto en otro
set1.symmetric_difference_update(set2)
print("Conjunto 1 después de symmetric_difference_update:", set1)

# Utilizar el método union para obtener la unión de conjuntos
union = set1.union(set2)
print("Unión entre conjunto 1 y conjunto 2:", union)

# Utilizar el método update para actualizar un conjunto con la unión del conjunto con otros
set1.update(set2)
print("Conjunto 1 después de update:", set1)


# frutas = ('platano', 'manzana', 'naranja')
# print(type(frutas))
# frutas_set = set(frutas)
# print(type(frutas_set))
# print(frutas_set)