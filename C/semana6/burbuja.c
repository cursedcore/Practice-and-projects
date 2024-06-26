#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

int main(void)
{
    int vector[10]={10,2,3,35,4,7,9,11,44,6};
    int a;
    system("clear");
    for(int i = 0; i < 10; i++)
    {
        for(int j = 0; j < 10; j++)
        {
            if(vector[j] > vector[j+1])
            {
                a = vector[j+1];
                vector[j+1] = vector[j];
                vector[j] = a;
            }
        }

    }
    for(int i = 1; i <= 10; i ++)
    {
        printf("%d ", vector[i]);
    }
    printf("\n");
    return 0;
}