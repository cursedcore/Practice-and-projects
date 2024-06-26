#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(void)
{
     int puntos;
    do
    {
        system("clear");
        puntos = get_int("Cuantos puntos perdiste?\n ");
        if(puntos >= 0 && puntos < 2)
        {
            system("clear");
            printf("Perdiste menos puntos que yo\n");
        }
        else if(puntos > 2)
        {
            system("clear");
            printf("Perdiste mas puntos que yo\n");
        }
        else if(puntos == 2)
        {
            system("clear");
            printf("Perdiste la misma cantidad de puntos que yo\n\n");
        }
    }
    while(puntos >= 0);

    return 0;
}