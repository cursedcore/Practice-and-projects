#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(void)
{
    system("clear");
    char a = 'a' , e ='e',i ='i', o = 'o', u = 'u';
    char letra = get_char("Escriba una letra: \n");
    system("clear");
    if(letra == a || letra == e || letra == i || letra == o || letra == u)
    {
        printf(" La letra '%c' es una vocal\n",letra);
    }
    else
    {
        printf("La letra '%c' no es una vocal\n", letra);
    }
    return 0;
}