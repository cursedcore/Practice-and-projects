#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

int main (void)
{
    int n;
    system("clear");
    do
    {
        n = get_int("Cuántas frutas desea comprar?\n ");
    }
    while(n < 1);
    string frutas[n];
    int p[n];
    for(int i = 0; i < n ; i++)
    {
        frutas[i] = get_string("Escriba el nombre de la fruta #%d: ", i+1);
        system("clear");

    }
     for(int i = 0; i < n; i++)
        {
            do
            {
                p[i] = get_int("Escriba el precio de %s: ", frutas[i]);
                system("clear");
            }
            while(p <= 0);
        }
    printf("-------------------------------\n");
    printf("Fruta                  Precio\n");
    printf("-------------------------------\n");
    for(int i = 0; i < n; i++)
    {
        printf("%s                    C$%d\n", frutas[i], p[i]);
        printf("-------------------------------\n");
    }

        return 0;
}