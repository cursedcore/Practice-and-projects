#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

float suma, resta, multiplicacion, division;

int main(void)
{
    float n1 = get_float("Escriba un numero: \n ");
    system("clear");
    float n2 = get_float("Escriba otro numero: \n ");
    system("clear");
    suma = n1 + n2;
    resta = n1 - n2;
    multiplicacion = n1 * n2;
    division = n1 / n2;
    printf("El resultado de la suma es: %.2f\n",suma);
    printf("El resultado de la resta es: %.2f\n", resta);
    printf("El resultado de la multiplicacion es: %.2f\n", multiplicacion);
    printf("El resultado de la division es: %.2f\n", division);

    return 0;
}
