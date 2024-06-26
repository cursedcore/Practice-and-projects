#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
// prototipado de funciones
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    system("clear");
    string text = get_string("Text: ");
    float L = (float)count_letters(text) / count_words(text) * 100;
    float S = (float)count_sentences(text) / count_words(text) * 100;
    int index;
    // formula para calcular el grado de dificultad
    index = round(0.0588 * L - 0.296 * S - 15.8);
    // imprimir el grado de dificultad
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
    return 0;
}
//funcion para contar letras
int count_letters(string text)
{
    int letras = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letras += 1;
        }
    }
    // printf("Letters: %d\n", letras);
    return letras;
}
//funcion para contar palabras
int count_words(string text)
{
    int palabras = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            palabras += 1;
        }
    }
    // printf("Words: %d\n", palabras);
    return palabras;
}
//funcion para contar oraciones
int count_sentences(string text)
{
    int oraciones = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            oraciones += 1;
        }
    }
    // printf("Sentences: %d\n", oraciones);
    return oraciones;
}