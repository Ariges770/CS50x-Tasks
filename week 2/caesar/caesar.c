#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>


bool only_digits(string key);
char rotate(char n, int encoder);


int main(int argc, string argv[])
{
    //if argc is 2 continue otherwise return 1
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //set key to user input
    string key = argv[1];

    //function to determine if key is a digit
    if (only_digits(key) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //convert key to int and convert to digit from 0-25
    int encoder = atoi(key) % 26;

    //get plaintext from user
    string plaintext = get_string("plaintext:  ");

    //function to rotate plaintext by encoder
    printf("ciphertext: ");
    for (int i = 0; i < strlen(plaintext); i++)
    {
        //set n to char of plaintext
        char n = plaintext[i];
        rotate(n, encoder);
    }
    printf("\n");
}

//function to ensure all chars in string are digits
bool only_digits(string key)
{
    for (int i = 0; i < strlen(key); i++)
    {
        if (isdigit(key[i]) == false)
        {
            return false;
        }
    }
    return true;
}

//function to encipher text
char rotate(char n, int encoder)
{
    if (isalpha(n) != false)
    {
        n = (int)n + encoder;
        if (isalpha(n) == false)
        {
            n = (int)n - 26;
        }
    }
    printf("%c", n);
    return 1;
}