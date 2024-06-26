#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        return 1;
    }
    BYTE bytes[512];
    char name[8];
    int contador = 0;
    FILE *jpg = NULL;
    while (fread(&bytes, sizeof(bytes), 1, file))
    {
        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
        {
            if (contador > 0)
            {
                fclose(jpg);
            }
            sprintf(name, "%03i.jpg", contador);
            jpg = fopen(name, "w");
            fwrite(bytes, sizeof(bytes), 1, jpg);
            contador++;
        }
        else if (contador > 0)
        {
            fwrite(bytes, sizeof(bytes), 1, jpg);
        }
    }
    fclose(file);
    if (jpg != NULL)
    {
        fclose(jpg);
    }
    return 0;
}