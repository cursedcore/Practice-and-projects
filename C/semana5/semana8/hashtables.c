#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <strings.h>
#include <string.h>

typedef struct node
{
    char word[46];
    struct node *next;
} node;

node *hashtable[26];
int hash(string palabra);
void insertar(string palabra);
void mostrar(void);
void buscar(string texto);
void free_hash(void);

int main(void)
{
    string dato;
    for (int i = 0; i < 5 ; i++)
    {
        dato = get_string("Ingrese una palabra: ");
        insertar(dato);
    }
    system("clear");
    mostrar();
    buscar("adamary");
    free_hash();

    return 0;
}
//funcion hash
int hash(string word)
{
    int hash = tolower(word[0]) - 'a';
    return hash;
}
void insertar(string palabra)
{
    node *nuevo_nodo = malloc(sizeof(node));
    if (nuevo_nodo == NULL)
    {
        return;
    }
    strcpy(nuevo_nodo->word, palabra);
    int pos = hash(palabra);
    if (hashtable[pos] == NULL)
    {
        nuevo_nodo->next = NULL;
        hashtable[pos] = nuevo_nodo;
    }
    else
    {
        nuevo_nodo->next= hashtable[pos];
        hashtable[pos] = nuevo_nodo;
    }
}
void mostrar(void)
{
    node *temp = NULL;
    for(int i = 0; i < 26; i++)
    {
        temp = hashtable[i];
        while(temp != NULL)
        {
            printf("%s\n", temp->word);
            temp = temp->next;
        }
    }
}
void buscar (string texto)
{
    int pos = hash(texto);
    node *actual = hashtable[pos];
    while(actual != NULL)
    {
        if (strcasecmp(texto, actual->word) == 0)
        {
            printf("Se encontró el dato que está buscando.\n");
            return;
        }
        actual = actual->next;
    }
    printf("No se encontró el dato.\n");
}
void free_hash(void)
{
    node *actual = NULL;
    node *eliminar = NULL;
    for (int i = 0; i < 26; i++)
    {
        actual = hashtable[i];
        while(actual != NULL)
        {
            eliminar = actual;
            actual = actual->next;
            free(eliminar);
        }
    }
}