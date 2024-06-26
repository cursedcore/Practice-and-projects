#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    system("clear");
    int n = get_int("Escriba un número: \n");
    int cuadrado = pow(n,2);
    int cubo = pow(n,3);
    printf("El cuadrado del número es: %d\n", cuadrado);
    printf("El cubo del número es: %d\n", cubo);

    return 0;
}