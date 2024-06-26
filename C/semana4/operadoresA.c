#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int num1 = 28, num2 = 7, num3 = 15, num4 = 3;
    system("clear");
    printf("num1: %d num2: %d num3: %d num4: %d\n", num1, num2, num3, num4);
    int mult = num1 * 3;
    printf("%d *  3 = %d\n", num1, mult);
    int suma = num1 + num2;
    printf("%d +  %d = %d\n", num1, num2, suma);
    int resta = num1 - num2;
    printf("%d -  %d = %d\n", num1, num2, resta);
    float div = (num1*1.0) / num3;
    printf("%d /  %d = %.2f\n", num1, num3, div);
    int div2 = num1 / num2;
    printf("%d /  %d = %d\n", num1, num2, div2);
    getchar();
    system("clear");
    printf("num1: %d num2: %d num3: %d num4: %d\n", num1, num2, num3, num4);
    printf("multiplicacion: %d\nsuma: %d\nresta: %d\ndivision (n1/n3): %.2f\ndivision (n1/n2): %d\n", mult, suma, resta, div, div2);
    return 0;
}