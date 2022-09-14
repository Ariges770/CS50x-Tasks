#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//listed functions in code
string get_text(void);
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);


int main(void)
{
    //recieves text and outputs values for letters, words and sentences
    string text = get_text();
    int letters = count_letters(text);
    float words = count_words(text);
    int sentences = count_sentences(text);


    //calculating L and S averages for Coleman-Liau index algo
    float L = 100 * (letters / words);
    float S = 100 * (sentences / words);

    //Coleman-Liau index equation
    float index = 0.0588 * L - 0.296 * S - 15.8;

    //rounding index to nearest int
    index = round(index);

    //Grade level of text based on output
    if (index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 1 && index < 16)
    {
        printf("Grade %d\n", (int)index);
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
}


string get_text(void)
{
    //text input
    string text = get_string("Text: ");
    return text;
}

int count_letters(string text)
{
    //count letters by using function to determin if char is a letter along an array of the string
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int count_words(string text)
{
    //count words by counting space characters in text array
    int words = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 32)
        {
            words++;
        }
    }
    return words + 1;
}

int count_sentences(string text)
{
    //counting sentences by adding periods, exclamation marks and question marks
    int sentences = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            sentences++;
        }
    }
    return sentences;
}