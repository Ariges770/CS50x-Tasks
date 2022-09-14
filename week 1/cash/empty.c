#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int change=0;
int dimes;
int nickels;
int pennies;

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // Request from usr how many cents
    int cents;
    do
        cents=get_int("How many cents do you have? ");
    while (cents<0);
    return cents;
}

int calculate_quarters(int cents)
{
    // TODO
    change += cents/25;
    return change;
}