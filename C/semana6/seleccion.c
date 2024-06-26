#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

void ordenar(int array[], int n);
void imprimir(int array[], int n);

int main(void)
{
    int arr[4] = {10, 5, 2};
    system("clear");
    printf("Datos no ordenados: \n");
    imprimir(arr, 3);
    ordenar(arr, 3);
    printf("\nDatos ordenados de forma ascendente: \n");
    imprimir(arr, 3);
    return 0;
}
void ordenar(int array[], int n)
{
    int position, swap;
    for (int i = 0; i < n - 1; i++)
    {
        position = i;
        for (int j = i + 1; j < n; j++)
        {
            if (array[position] > array[j])
            {
                position = j;
            }
        }
        if (position != i)
        {
            swap = array[i];
            array[i] = array[position];
            array[position] = swap;
        }
    }
}
void imprimir(int array[], int n)
{
    for(int i = 0; i < n; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");
}