#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
 
int main(int argc, char *argv[])
{
    // ensure that there is only one CL arg 
    if (argc != 2)
    {
        printf("./recover filename\n");
        return 1;
    }
    // set pointer to filename
    char *forensic_image = argv[1];

    FILE *inptr = fopen(forensic_image, "r");
    // ensure that file opened is valid
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", forensic_image);
        return 1;
    }

    BYTE block = 512 * block;

    int *buffer = calloc(sizeof(block), 0);

    int i = 0;

    while (fread(buffer, block, 1, inptr) == block)
    {
        
    }

    printf("hi\n");

    free(buffer);

    return 0;
}