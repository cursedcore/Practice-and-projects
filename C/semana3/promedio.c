#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

float prom;


int main(void)
{
    char a = '%';
    system("clear");
    int nota1 = get_int("Ingrese su primera nota: \n ");
    system("clear");
    int nota2 = get_int("Ingrese su segunda nota: \n ");
    system("clear");
    int nota3 = get_int("Ingrese su tercera nota: \n ");
    system("clear");
    prom = (nota1 + nota2 + nota3)/3;

    if(prom >= 60)
    {
        printf("Aprobaste, tu promedio es: %.2f%c\n",prom,a );
    }
    else
    {
        printf("Reprobaste, tu promedio es: %.2f%c\n", prom, a);
    }
    return 0;
}