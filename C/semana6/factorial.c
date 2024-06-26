#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

//Angel Amaru Montenegro Munguía. Grupo F.

bool only_digits(string text);
int factorial_while(int k);
int factorial_for(int k);

int main(int argc, string argv[])
{
    int k, tamaño;
    system("clear");
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Uso: ./factorial numero\n");
        return 1;
    }
    k = atoi(argv[1]);

    printf("Con while: %d! = %d\n", k, factorial_while(k));
    printf("Con for: %d! = %d\n", k, factorial_for(k));

    return 0;
}

bool only_digits(string text)
{
    int tamaño;
    tamaño = strlen(text);
    for (int i = 0; i < tamaño; i++)
    {
        if (!isdigit(text[i]))
        {
            return false;
        }
    }
    return true;
}
int factorial_while(int n)
{

    int wfact = 1;
    int i = 1;

    while(i <= n)
    {
        wfact = wfact * i;
        i ++;
    }
    return wfact;
}
int factorial_for(int n)
{
    int ffact = 1;
    for (int i = 1; i <= n; i++)
    {
        ffact = ffact * i;
    }

    return ffact;
}