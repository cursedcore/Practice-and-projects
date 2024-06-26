#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    system("clear");
    float n1 = get_float("Escriba un número decimal: ");
    system("clear");
    float n2 = get_float("Escriba otro número decimal: ");
    system("clear");
    float div = n1 / n2;
    printf("El resultado de la división es: %.2f\n" ,div);

    return 0;
}