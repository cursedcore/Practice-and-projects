#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(void)
{
    system("clear");
    float x = get_float("x: ");
    float y = get_float("y: ");
    float z = x / y;

    printf("%.50f\n",z);
    return 0;
}
