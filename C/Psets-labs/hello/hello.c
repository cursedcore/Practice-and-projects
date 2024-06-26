#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    system("clear");
    string name = get_string("Escribe tu nombre: \n");
    system("clear");
    printf("hello, %s\n", name);

    return 0;
}
