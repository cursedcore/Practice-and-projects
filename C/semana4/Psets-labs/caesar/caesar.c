#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
// prototipo de las funciones
bool only_digits(string text);
char rotate(char P, int k);

int main(int argc, string argv[])
{
    int k, tamaño;
    string plaintext;
    // validar que solo puedan haber enteros en la posicion 1 de la terminal
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // convertir arreglo a entero
    k = atoi(argv[1]);

    plaintext = get_string("plaintext: ");

    tamaño = strlen(plaintext);
    char ciphertext[tamaño + 1];
    // rotar el texto para cifrarlo
    for (int i = 0; i < tamaño; i++)
    {
        ciphertext[i] = rotate(plaintext[i], k);
    }
    // indicar que el string ha terminado
    ciphertext[tamaño] = '\0';
    // mostrar el texto ya cifrado
    printf("ciphertext: %s\n", ciphertext);
    return 0;
}
// funcion para que solo se puedan poner digitos
bool only_digits(string text)
{
    int tamaño;
    tamaño = strlen(text);
    for (int i = 0; i < tamaño; i++)
    {
        if (!isdigit(text[i]))
        {
            return false;
        }
    }
    // retornar un valor booleano
    return true;
}
// funcion para rotar el string de enteros
char rotate(char P, int k)
{
    char Pi, C, Ci;
    // caso de las mayusculas
    if (isupper(P))
    {
        Pi = P - 65;
        Ci = (Pi + k) % 26;
        C = Ci + 65;
    }
    // caso de minusculas
    else if (islower(P))
    {
        Pi = P - 97;
        Ci = (Pi + k) % 26;
        C = Ci + 97;
    }
    else
    {
        return P;
    }
    return C;
}