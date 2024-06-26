from cs50 import get_string
import os
os.system("clear")

palabra = get_string("ingrese cualquier cosa: ")

Letras = 0
Oraciones = 1
Palabras = 1

for i in range(len(palabra)):
    if palabra[i].isalpha():
        Letras += 1
    elif palabra[i].isspace():
        Palabras += 1
    elif palabra[i] == '.' or palabra[i] == '?' or palabra[i] == '!':
        Oraciones += 1
print(f"El texto tiene {Letras} letras, {Oraciones} oraciones y {Palabras} palabras")

