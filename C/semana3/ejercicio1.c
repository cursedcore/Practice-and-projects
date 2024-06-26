#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(void)
{
    int num;
    do
    {
        system("clear");
        num = get_int("Ingrese un numero mayor que 10, y menor que 100: \n");
        system("clear");
        printf("%d\n", num);

    }
    while(num < 10 || num > 100);
    return 0;
}