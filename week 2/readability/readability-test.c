#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


string get_text(void);
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);


int main(void)
{
string text = get_text();
int letters = count_letters(text);
float words = count_words(text);
int sentences = count_sentences(text);


float L = 100*(letters/words);
float S = 100*(sentences/words);

float index = 0.0588 * L - 0.296 * S -15.8;
printf("index %f \n", index);
index = round(index);
if (index <= 1)
{
    printf("Before Grade 1\n");
}
else if (index > 1 && index < 16)
{
    printf("Grade %f\n", index);
}
else if (index >= 16)
{
    printf("Grade 16+\n");
}
}


string get_text(void)
{
    string text = get_string("Text: ");
    return text;
}

int count_letters(string text)
{
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