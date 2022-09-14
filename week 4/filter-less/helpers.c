#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // for the height
    for (int i = 0; i < height; i++)
    {
        // for the width
        for (int j = 0; j < width; j++)
        {
            // find avg of rgb values
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int red = image[i][j].rgbtRed;
            // set all rgb to int avg
            float avg = (blue + green + red) / 3.0;
            image[i][j].rgbtBlue = round(avg);
            image[i][j].rgbtGreen = round(avg);
            image[i][j].rgbtRed = round(avg);
        }
    }
    // paste to the location of the pixel
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float origRed = image[i][j].rgbtRed;
            float origGreen = image[i][j].rgbtGreen;
            float origBlue = image[i][j].rgbtBlue;

            float sepiaRed = 0.393 * origRed + 0.769 * origGreen + 0.189 * origBlue;
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            float sepiaGreen = 0.349 * origRed + 0.686 * origGreen + 0.168 * origBlue;
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            float sepiaBlue = 0.272 * origRed + 0.534 * origGreen + 0.131 * origBlue;
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = (int)round(sepiaRed);
            image[i][j].rgbtGreen = (int)round(sepiaGreen);
            image[i][j].rgbtBlue = (int)round(sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // swap equivalent values from each side
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Allocate memory for copy
    RGBTRIPLE(*copy)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // copy image to copy
            copy[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // initialise values
            float totalred = 0;
            float totalgreen = 0;
            float totalblue = 0;
            float total = 0;
            int a;
            int b;
            int c;
            int d;

            // for top and bottom pixel, reduce height of blur averages
            if (i == 0)
            {
                a = 0;
                b = 1;
            }
            else if (i == height - 1)
            {
                a = 1;
                b = 0;
            }
            else
            {
                a = 1;
                b = 1;
            }
            // for left and right pixel, reduce width of blur averages
            if (j == 0)
            {
                c = 0;
                d = 1;
            }
            else if (j == width - 1)
            {
                c = 1;
                d = 0;
            }
            else
            {
                c = 1;
                d = 1;
            }
            for (int h = -a; h <= b; h++)
            {
                for (int w = -c; w <= d; w++)
                {
                    totalred += copy[i + h][j + w].rgbtRed;
                    totalgreen += copy[i + h][j + w].rgbtGreen;
                    totalblue += copy[i + h][j + w].rgbtBlue;
                    total += 1.0;
                }
            }
            image[i][j].rgbtRed = round(totalred / total);
            image[i][j].rgbtGreen = round(totalgreen / total);
            image[i][j].rgbtBlue = round(totalblue / total);
        }
    }
    free(copy);
    return;
}
