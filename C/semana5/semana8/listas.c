#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int main (void)
{
    node *list = NULL;
    //crear el primer nodo
    node *n1 = malloc(sizeof(node));
    if (n1 != NULL)
    {
        n1->number = 1;
        n1->next = NULL;
        list = n1;
        //hacer que list apunte al primer nodo
    }
    //crear el segundo nodo
    node *n2 = malloc(sizeof(node));
    if (n2 != NULL)
    {
        n2->number = 2;
        n2->next = NULL;
        n1->next = n2;
        //conectar el primer nodo con el segundo
    }
    //imprimir los valores de los nodos
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }
    //liberar la memoria utilizada por la lista
    while(list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
    return 0;
}