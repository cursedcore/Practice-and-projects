#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void)
{
    system("clear");
    char c = get_char("Escriba una letra: \n");
    system("clear");

    if(islower(c))
    {
        printf("Es minúscula\n");
    }
    else if(isupper(c))
    {
        printf("Es mayúscula\n");
    }
    else
    {
        printf("No es una letra\n");
    }
    return 0;
}