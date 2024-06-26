#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    int j = 0;
    system("clear");
    int est = get_int("Cuántos estudiantes hay en el aula?\n");
    system("clear");
    for (int i = 0; i < est; i++)
    {
        int prom = get_int("Escriba el promedio del estudiante #%d\n", i+1);
        system("clear");
        if(prom >= 60)
        {
            j++;
        }
    }
    printf("Han aprobado %d estudiantes\n", j);
    return 0;
}