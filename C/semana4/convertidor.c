#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <math.h>

int main (void)
{
    int ans; float money, c1, c2, c3, c4;
    system("clear");
    do
    {
        system("clear");
        printf("\t\t\t\tQué conversión desea hacer?\n");
        ans = get_int("\t\t\t\t1.Dólar a córdobas\n\t\t\t\t2.Córdobas a dólares\n\t\t\t\t3.Euros a córdobas\n\t\t\t\t4.Córdobas a euros\n\t\t\t\t");
    }
    while (ans < 1 || ans > 4);
    switch (ans)
    {
        case 1:
            do
            {
                system("clear");
                money = get_float("Ingrese la cantidad de dólares a convertir:\n");
            }
            while (money <= 0);
            c1 = round(money * 36.4);
            system("clear");
            printf("$%.2f = C$%.2f\n\n", money, c1);
            break;
        case 2:
            do
            {
                system("clear");
                money = get_float("Ingrese la cantidad de córdobas a convertir:\n");
            }
            while (money <= 0);
            c2 = round(money / 36.4);
            system("clear");
            printf("C$%.2f = $%.2f\n\n", money, c2);
            break;
        case 3:
            do
            {
                system("clear");
                money = get_float("Ingrese la cantidad de euros a convertir:\n");
            }
            while (money <= 0);
            c3 = round(money * 38.39);
            system("clear");
            printf("€%.2f = C$%.2f\n\n", money, c3);
            break;
         case 4:
            do
            {
                system("clear");
                money = get_float("Ingrese la cantidad de córdobas a convertir:\n");
            }
            while (money <= 0);
            c4 = round(money / 36.4);
            system("clear");
            printf("C$%.2f = €%.2f\n\n", money, c4);
            break;
    }
    return 0;
}