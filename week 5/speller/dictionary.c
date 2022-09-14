// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h> 
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Word count added to dictionary
int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

node *insert_node(node *head, char *new_word);

// TODO: Choose number of buckets in hash table
const unsigned int N = 50000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Set var for which index of array to search
    int hash_index = hash(word);

    if (table[hash_index] == NULL)
    {
        return false;
    }


    node *curser = table[hash_index];

    while (curser != NULL)
    {       
        if (strcasecmp(word, curser -> word) == 0)
        {
            return true;
        }
        curser = curser -> next;
    }
    return false;
}

// Hashes word to a number through adding letter values, squaring the total and taking the remainder when divided by N
unsigned int hash(const char *word)
{
    int total = 0;
    // Set seed as large prime
    int seed = 401;

    for (int i = 0; word[i] != '\0'; i++)
    {
        total += (tolower(word[i]));
    }
    total = (total * total * seed) % N;
    return total;
    
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file

    FILE *dictionary_list = fopen(dictionary, "r");
    if (dictionary_list == NULL)
    {
        return false;
    }

    char *temp_word = malloc(LENGTH + 1);
    if (temp_word == NULL)
    {
        return false;
    }
    int hash_key = 0;
    int counter = 0;

    // Read strings from file one at a time

    while (fscanf(dictionary_list, "%s", temp_word) != EOF)
    {
            hash_key = hash(temp_word);
            table[hash_key] = insert_node(table[hash_key], temp_word);

            if (table[hash_key] == NULL)
            {
                return false;
            }

            // Adds 1 to word count to use in size function
            word_count++;
    }

    free(temp_word);
    fclose(dictionary_list);
    return true;
    // Insert node into hash table at that location
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Returns the word count from load function
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *p = table[i] -> next;
            free(table[i]);
            table[i] = p;
        } 
        
        table[i] = NULL;

    }
    return true;
}

node *insert_node(node *head, char *new_word)
{
    node *new_node = malloc(sizeof(node));
    if (new_node == NULL)
    {
        return NULL;
    }
    strcpy(new_node -> word, new_word);
    
    new_node -> next = head;
    return new_node;
}