#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int nprimo(int n);

int main(void)
 {
    system("clear");
    int i = 0;
    int inicio = 0, fin = 30;
    printf("Los números primos del 1 al 30 son:\n");
    for (int x = inicio; x <= fin; x++)
    {
        if (nprimo(x))
        {
            i++;
            printf("%d ", x);
        }
    }
    printf("\n\n");
    return 0;
}

int nprimo(int n)
{
  if (n == 0 || n == 1)
  {
    return 0;
  }
  if (n == 4)
  {
    return 0;
  }

  for (int x = 2; x < n / 2; x++)
  {
    if (n % x == 0)
    return 0;
  }
  return 1;
}