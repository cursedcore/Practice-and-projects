#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
/*Este programa sirve para calcular el cuadrado de los numeros del 1 al 10*/
int main(void)
{
    system("clear");
    for(int i = 1 ;i < 11 ;i++)
    {
       int n = i * i;
       printf("El cuadrado de %d es: %d\n",i,n);
    }
    return 0;
}