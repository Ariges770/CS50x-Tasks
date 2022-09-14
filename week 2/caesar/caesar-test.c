#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{
    char n = get_char("letter: ");
    int encoder = get_int("key: ");
    if (isalpha(n) != false)
    {
        printf("hi\n");
        n = (int)n + encoder;
        if (isalpha(n) == false)
        {
            n = (int)n - 26;
        }
    }
    printf("letter %c\n", n);
}