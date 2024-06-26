#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

long factorial(int n);

int main(void)
{
    system("clear");
    int numero = get_int("Escriba un numero: ");
    long fact = factorial(numero);
    printf("%d! = %ld\n", numero, fact);
    return 0;
}
long factorial(int n)
{
    if (n == 0)
    {
        return 1;
    }
    else
    {
        return n * factorial(n - 1);
    }
}
