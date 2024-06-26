#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int j, n, i, k, space;
    system("clear");
    //pedir la altura al usuario
    do
    {
        n = get_int("Height: \n");
        space = n - 1;
    }
    while (n < 1 || n > 8);
    //imprimir la altura
    for (i = 0; i < n; i++)
    {
        //imprimir espacios
        for (k = space; i < k; k--)
        {
            printf(" ");
        }
        printf("#");
        //imprimir anchura
        for (j = 0; j < i ; j++)
        {
            printf("#");
        }

        printf("\n");
    }
    return 0;
}
