#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int inicial, final, años = 0, yo;
    // TODO: Prompt for start size
    do
    {
        system("clear");
        inicial = get_int("Ingrese el tamaño inicial de la poblacion: ");
    }
    while (inicial < 9);
    // TODO: Prompt for end size
    do
    {
        system("clear");
        final = get_int("Ingrese el tamaño final de la poblacion: ");
    }
    while (final < inicial);
    // TODO: Calculate number of years until we reach threshold
    if (final == inicial)
    {
        system("clear");
        printf("Years: %d\n", años);
    }
    else
    {
        while (inicial < final)
        {
            system("clear");
            inicial = inicial + (inicial / 3) - (inicial / 4);
            años++;
        }
        // TODO: Print number of years
        printf("Years: %d\n", años);
    }
    return 0;
}