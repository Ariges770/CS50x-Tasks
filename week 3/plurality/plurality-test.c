void print_winner(void)
{
    string highest[] = {0};
    int w = 0;
    // Change TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > candidates[i].votes)
        {
            highest[w] = candidates[i + 1].name;
            printf("%s", highest[w]);
            w +=1;
        }
    }
    for (int i = 0; i < w; i++)
    {
        printf("%s\n", highest[i]);
    }
    return;
}