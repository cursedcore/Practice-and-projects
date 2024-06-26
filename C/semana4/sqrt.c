#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    float raiz;
    system("clear");
    int n = get_int("Escriba un número: \n");
    raiz = round(sqrt(n));
    printf("La raíz cuadrada de %d es: %.1f\n", n, raiz);
    return 0;
}