#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //list of variables used
    int h;
    int i;
    int j;
    int k;
    //request height from user until between 1-8
    do
    {
        h = get_int("Pyramid height: ");
    }
    while (h < 1 || h > 8);
    //loop to build pyramid based on height (h)
    for (i = 1; i <= h; i++)
    {
        for (k = h; k > i; k--)
        {
            //spaces on pyramids left
            printf(" ");
        }
        for (j = 1; j < i; j++)
        {
            //hashes from the pyramids right
            printf("#");
        }
        //last hash and line break
        printf("#\n");
    }
}