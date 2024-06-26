#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    system("clear");
    printf("Números pares entre 0 y 30: \n");
    for(int i = 0; i < 31; i +=2)
    {
        printf("%d\n", i);
    }
    return 0;
}