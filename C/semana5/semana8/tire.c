#include <stdlib.h>
#include <stdio.h>
//Definir la estructura del nodo del trie
typedef struct node
{
    bool is_word;
    struct trie_node *children[26];
} trie_node;

//funcion para crear un nuevo nodo en el trie
trie_node *create_node()
{
    trie_node *new_node = (trie_node*)malloc(sizeof(trie_node));
    new_node->is_word = false;
    for (int i = 0; i < 26; i++)
    {
        new_node->children[i] = NULL;
    }
    return new node;
}
//funcion para insertar una palabra en el trie
void insert (trie_node *root, char *word)
{
    trie_node *current = root;
    for (int i = 0; i < strlen(word); i++)
    {
        int index = word[i] - 'a';
        if (current ->children[index] == NULL)
        {
            current ->children[index] = create_node();
        }
        current = current->children[index];
    }
    current->is_word = true;
}
//buscar palabra en el trie
bool search(trie_node *root, char *word)
{
    trie_node *current = root;
    for (int i = 0; i < strlen(word); i++)
    {
        int index = word[i] -'a';
        if (current ->children[index] == NULL)
        {
            return false;
        }
        current = current->children[index];
    }
    return current != NULL && current->is_word;
}

//funcion principal
int main (void)
{
    trie_node *root = create_node();
    char *words[] = {"car", "cart", "cat","cats","dog"};
    for (int i = 0; i < sizeof(words) / sizeof(words[0]); i++)
    {
        insert(root, words[i]);
    }
    
    return 0;
}