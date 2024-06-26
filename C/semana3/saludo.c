#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(void)
{
    system("clear");
    string nombre = get_string("Escribe tu nombre: \n");
    printf("Hola %s, mucho gusto! ^.^ \n",nombre);
    return 0;
}