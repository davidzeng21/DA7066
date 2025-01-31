# Task 1: Loading a sequence database from multiple files
def check_dna(seq):
    # Verifies that the sequence contains only valid DNA characters.
    if len(set(seq) - set({'T', 'A', 'G', 'C'})) > 0:
        raise ValueError("DNA sequnece {0} contains at least one invalid character".format(seq))

def read_fasta(f):
    # Reads a FASTA file and returns a dictionary of sequences.
    sequences = {}
    with open(f, 'r') as file:
        for line in file:
            if line.startswith('>'): # Header line
                name = line.rstrip()
                sequences[name] = ''
            else:
                seq = line.rstrip() # Sequence line
                check_dna(seq)
                sequences[name] += seq
    return sequences

def add_to_database(d,f):
    # Adds sequences from file 'f' into the existing database dictionary 'd'.
    sequences = read_fasta(f) # Read sequences from file
    d[f] = sequences # Add sequences to the database
    return d

# Task 2: Analyzing all records from a species

def filter_seqs(database, species):
    # Filters and returns sequences from the specified species.
    filtered = {}
    for file in database:
        for name in database[file]: # Iterate over sequences in the file
            if species in name: # Check if the species is in the sequence name
                filtered[name] = database[file][name] # Add the sequence to the filtered dictionary
    return filtered

def total_sequence_length(d):
    # Calculates the total length of all sequences in the given dictionary.
    # Raise an error if the input is not a dictionary
    if type(d) is not dict: 
        raise ValueError("Input must be a dictionary") 
    total = 0 
    for seq in d.values(): # Iterate over sequences in the dictionary
        total += len(seq) 
    
    return total

# Task 3: Writing a dictionary to a fasta file

def write_fasta(d, f):
    # Writes all sequences in the dictionary 'd' to a FASTA file 'f'.
    with open(f, 'w') as file: 
        for name, seq in d.items(): # Iterate over sequences in the dictionary
            file.write(name + '\n')
            file.write(seq + '\n')

# Task 4: Putting it all together

def main():
    # Main function to interact with the user and perform selected tasks.
    d = {}
    print("(a) add a file to the database;")
    print("(b) print the length of all sequences of a given species;")
    print("(c) write out a fasta file of all sequences of a given species;")
    print("(q) quit;")
    while True:
        # Loop to handle user input and perform tasks.
        opt = input("Provide an option: ")
        if opt == 'a':
            # Option 'a' for adding a file to the database.
            while True:
                try:
                    f = input("Provide file path: ")
                    d = add_to_database(d, f)
                    break
                except FileNotFoundError as e:
                    print(f"File not found error: {e}. Please provide a valid file path.")
                except ValueError as e:
                    print(f"Invalid sequence error: {e}. Please provide a valid FASTA file.")
        elif opt == 'b':
            # Option 'b' for printing total sequence length of a given species.
            species = input("Which species: ")
            filtered = filter_seqs(d, species)
            print(total_sequence_length(filtered))
        elif opt == 'c':
            # Option 'c' for writing out a FASTA file of filtered sequences.
            species = input("Enter the species: ")
            filepath = input("Which file path: ")
            filtered = filter_seqs(d, species)
            write_fasta(filtered, filepath)
            print("File saved.")
        elif opt == 'q':
            # Option 'q' to quit.
            print("Goodbye!")
            break
        else:
            # Handle invalid inputs.
            print("Invalid option. Try again.")


if __name__ == '__main__':
    main()









