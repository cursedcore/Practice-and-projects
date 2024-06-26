# Utilizar el diccionario persona
persona = {
    "nombre": "Amaru",
    "edad": 40,
    "ciudad": "Estelí",
    "hobbies": ["deporte", "música", "lectura"]
}
print("Diccionario inicial:", persona)

# Utilizar el método clear para eliminar todos los elementos del diccionario
persona.clear()
print("Diccionario después de clear:", persona)

# Crear un nuevo diccionario
persona = {
    "nombre": "Amaru",
    "edad": 40,
    "ciudad": "Estelí",
    "hobbies": ["deporte", "música", "lectura"]
}
print("Diccionario original:", persona)

# Utilizar el método copy para obtener una copia del diccionario
copia_persona = persona.copy()
print("Copia del diccionario:", copia_persona)

# Utilizar el método fromkeys para crear un nuevo diccionario con claves y valores específicos
claves = ["a", "b", "c"]
valores = "desconocido"
nuevo_diccionario = dict.fromkeys(claves, valores)
print("Nuevo diccionario con fromkeys:", nuevo_diccionario)

# Utilizar el método get para obtener el valor de una clave específica
edad = persona.get("edad")
print("Valor de la clave 'edad':", edad)

# Utilizar el método items para obtener una lista de tuplas con las parejas clave-valor
items = persona.items()
print("Parejas clave-valor del diccionario:", items)

# Utilizar el método keys para obtener una lista con las claves del diccionario
claves = persona.keys()
print("Claves del diccionario:", claves)

# Utilizar el método pop para eliminar un elemento con una clave específica
valor_eliminado = persona.pop("edad")
print("Valor eliminado con pop:", valor_eliminado)
print("Diccionario después de pop:", persona)

# Utilizar el método popitem para eliminar la última entrada insertada
elemento_eliminado = persona.popitem()
print("Elemento eliminado con popitem:", elemento_eliminado)
print("Diccionario después de popitem:", persona)

# Utilizar el método setdefault para obtener el valor de una clave o crearla si no existe
profesion = persona.setdefault("profesion", "Desconocido")
print("Valor de la clave 'profesion':", profesion)

# Utilizar el método update para actualizar el diccionario con nuevos pares clave-valor
persona.update({"ciudad": "Barcelona", "profesion": "Ingeniero"})
print("Diccionario después de update:", persona)

# Utilizar el método values para obtener una lista con todos los valores del diccionario
valores = persona.values()
print("Valores del diccionario:", valores)
