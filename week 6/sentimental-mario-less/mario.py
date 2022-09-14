from cs50 import get_int 

# Initialise height value
height = 0 

# Ensure height input from user is between 1 and 8
while height < 1 or height > 8:
    height = get_int("how tall is the pyramid? ")

# Print out spaces and hash's for pyramid
for i in range(1, height + 1):
    print(" " * (height - i) + ("#" * i))