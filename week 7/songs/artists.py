import os
import csv 
from sys import argv, exit

def main():

    # Create list of artists from csv
    artists = []
    with open("artists.csv") as infile:
        for song in csv.DictReader(infile):
            try:
                if song["Artist"] not in artists:
                    artists.append(song["Artist"])
            except:
                print("Error: No 'Artist' column in csv file \nError: 1")
                exit(1)
    if (len(argv) != 2):
        print("Error: python artists.py create/rm")
        print("Error: 2")
        exit(2)


    # Determine operation as whether to make/rm from user input
    if (argv[1] == "create"):
        create_folders(artists)
    elif (argv[1] == "rm"):
        delete_folders(artists)
    else:
        print("Error: python artists.py create/rm")
        print("Error: 3")
        exit(3)

    # Alert user if the program worked as intended
    print("Passed")



# Creates dir for artist directories then creates them inside from provided list
def create_folders(list):     
    try:
        os.mkdir("artists")
    except:
        pass
    for index in range(len(list)):
        try:
            os.mkdir(f"artists/{list[index]}")
        except:
            pass


# Searches inside artists dir for the expected directory and if it finds, deletes then deletes parent dir
def delete_folders(list):
    for index in range(len(list)):
        try:
            os.rmdir(f"artists/{list[index]}")
        except:
            pass
    
    try:
        os.rmdir("artists")
    except:
        print("Error: Failed to remove test directory \nError: 4")
        exit(4)


if __name__ == "__main__":
    main()
