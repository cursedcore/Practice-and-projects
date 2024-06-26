#include <stdio.h>
#include <cs50.h>

//ctrl + k + c para comentarear
//ctrl + k + u para descomentarear
//ctrk + k + q para seleccionar

int main (int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Ingrese la cantidad de arg correcta!");
    }
    // int cantidad = argc;
    // printf("%d\n", cantidad);
    for (int i = 0; i < 4; i++)
    {
        printf("%s", argv[i]);
    }
    printf("\n");
    return 0;
}
