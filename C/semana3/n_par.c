#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(void)
{
    int yo;
    system("clear");
    int n = get_int("Ingrese un numero entero: \n ");
    yo = n%2;
    system("clear");
    if(yo == 1)
    {
        printf("El numero %d es impar\n",n);
    }
    if(yo == 0)
    {
        printf("El numero %d es par\n",n);
    }
    return 0;
}