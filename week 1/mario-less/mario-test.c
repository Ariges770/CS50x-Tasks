#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int i;
    int j;
    int k;
    for (i=1; i<=5; i++)
    {
        for (k=5; k>i; k--)
        {
            printf(" ");
        }
        for (j=1; j<i; j++)
        {
            printf("#");
        }
        printf("#\n");
    }
    printf("\n");
}