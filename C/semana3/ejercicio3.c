#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(void)
{
    int resultado;
    system("clear");
    int num = get_int("Escriba un numero: \n");
    system("clear");
    for(int i = 0; i < 13; i++)
    {
        resultado = num * i;
        printf("%d x %d = %d\n",i, num, resultado);
    }
    return 0;
}
