import csv
from fileinput import filename
import sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print("'Error: python dna.py *.csv *.txt'")
        return 1
    
    # TODO: Read database file into a variable
    filename = sys.argv[1]

    # Save name and str patterns to sequences list
    with open(filename, 'r') as header:
        for sequences in csv.reader(header):
            break

    max_STR_counts = {sequences[x]: 0 for x in range(1, len(sequences))}

    # Save csv database to the database list with each person having their own dictionary
    database = []
    with open(filename, 'r') as reader:
        for row in csv.DictReader(reader):
            database.append(row)

    # TODO: Read DNA sequence file into a variable
    filename = sys.argv[2]
    with open(filename, 'r') as dna_file:
        dna_sample = dna_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    STR_type_count = len(max_STR_counts)
    for x in range(STR_type_count):
        sequence_type = sequences[x + 1]
        max_STR_counts[sequence_type] = longest_match(dna_sample, sequence_type)

    # TODO: Check database for matching profiles

    # For each person of each sequence type
    matching_person = "No match"
    for person in range(len(database)):
        matches = 0
        compare_person = {sequences[pattern]: database[person][sequences[pattern]] for pattern in range(1, len(sequences))}

        for counter in range(1, len(sequences)):
            dna_type = sequences[counter]
            a = int(compare_person[dna_type])
            b = int(max_STR_counts[dna_type])
            if a == b:
                matches += 1

        if matches == int(len(sequences) - 1):
            matching_person = database[person]["name"]
            break
    print(matching_person)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
