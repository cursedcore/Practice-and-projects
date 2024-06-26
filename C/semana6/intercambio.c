#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
//Angel Amaru Montenegro Munguía. Grupo F.
int main(void)
{
    system("clear");
    int a = get_int("Escriba el valor de a: \n");
    int b = get_int("Escriba el valor de b: \n");
    system("clear");

    printf("Valores originales:\na = %d\nb = %d\n", a, b);

    a = a + b;
    b = a - b;
    a = a - b;

    printf("\nValores intercambiados:\na = %d\nb = %d\n", a, b);
    return 0;
}