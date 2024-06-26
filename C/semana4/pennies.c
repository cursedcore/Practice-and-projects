#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <math.h>
int main(void)
{
    system("clear");
    float amount = get_float("Dollar amount: ");
    int pennies = round(amount * 100);

    printf("Pennies: %d\n", pennies);
    return 0;
 }