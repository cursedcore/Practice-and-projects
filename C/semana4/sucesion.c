#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n = 1;
    system("clear");
    printf("%d ",n);
    for(int i = 0; i < 5; i ++)
    {
        n = n * 10;
        printf("%d ",n);
    }
    printf("\n\n");

    return 0;
}