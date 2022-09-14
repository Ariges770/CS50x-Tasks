from ast import Expression
from curses.ascii import isalpha
from cs50 import get_string

phrase = get_string("Input text here: ")

# Create dict to track letter, words and sentences
amounts = {
    "letters": 0,
    "words": 0,
    "sentences": 0
}

# Iteration over each letter in the phrase
for i in range(len(phrase)):
    letter = phrase[i]

    # Check if its a letter
    if letter.isalpha():
        amounts["letters"] += 1
    # Check if uts a word
    if letter == " ":
        amounts["words"] += 1
    # Check if its a space
    if letter in [".", "!", "?"]:
        amounts["sentences"] += 1

    # Add to wrod count at the end of the phrase to compensate for lacking space
    if (i + 1) == len(phrase):
        amounts["words"] += 1

# Calculate averages and index
L = 100 * (amounts["letters"] / amounts["words"])
S = 100 * (amounts["sentences"] / amounts["words"])

index = round((0.0588 * L) - (0.296 * S) - 15.8)

# Print grade level determined by index
if index < 1:
    print("Before Grade 1")
elif index > 1 and index < 16:
    print(f"Grade {index}")
else:
    print("Grade 16+")

