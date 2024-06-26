"""try:
    x = int(input("x: "))
except ValueError:
    print("That is not an int!")
    exit()

try:
    y = int(input("y:"))
except ValueError:
    print("That is not an int!")
    exit()

print(x + y)"""
from cs50 import get_int
numero1 = get_int("Ingrese el primer numero: ")
numero2 = get_int("Ingrese el segundo numero: ")
resultado = numero1 + numero2
print("La suma es:", resultado)
