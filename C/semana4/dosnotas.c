#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
int main(void)
{
    float prom;
    int n1, n2;
    char a = '%';
    system("clear");
    do
    {
        n1 = get_int("Escriba su primer nota: \n");
        system("clear");
    }
    while(n1 < 0 || n1 > 100);

    do
    {
        n2 = get_int("Escriba su segunda nota: \n");
        system("clear");
    }
    while(n2 < 0 || n2 > 100);

    prom = (n1 + n2)/2;

    if(prom >= 60)
    {
    printf("Aprobate, el promedio de ambas notas es: %.2f%c\n",prom,a);
    }
    else
    {
        printf("Reprobaste, tu promedio es: %.2f%c\n", prom,a);
    }
    return 0;
}