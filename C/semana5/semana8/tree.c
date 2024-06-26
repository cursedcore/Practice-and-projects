#include <stdlib.h>
#include <stdio.h>

typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
} node;
int main(void)
{
        node * tree = NULL;
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }
        n->number = 4;
        n->left = NULL;
        n->right = NULL;

        tree = n;
        //agregar nuevo nodo
        node *n2 = malloc(sizeof(node));
        if (n2 == NULL)
        {
            return 1;
        }
        n2->number = 2;
        n2->left = NULL;
        n2->right = NULL;

        if(n2->number < n->number)
        {
            n->left = n2;
        }
        else
        {
            n->right = n2;
        }
        //nodo 3
        node *n3 = malloc(sizeof(node));
        if (n3 == NULL)
        {
            return 1;
        }
        n3->number = 6;
        n3->left = NULL;
        n3->right = NULL;

        if(n3->number < n->number)
        {
            n->left = n3;
        }
        else
        {
            n->right = n3;
        }


        return 0;
}

void print_tree(node *root)
{
    if (root == NULL)
    {
        return;
    }
    print_tree(root->left);
    printf("");
}
void free_tree(node *root)
{
    if (root == NULL)
    {
        return;
    }
    free_tree();
    free_tree();
    free();
}
bool search(node *tree, int number)
{
    if (root == NULL)
    {
        return;
    }

    return true;
}