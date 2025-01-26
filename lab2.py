# Task 1: Loading a sequence database from multiple files

def read_fasta(f):
    '''Reads a FASTA file f and returns a dictionary of sequences.'''
    def check_dna(seq):
        if len(set(seq) - set({'T', 'A', 'G', 'C'})) > 0:
            raise ValueError("DNA sequnece {0} contains at least one invalid character".format(seq))
    
    sequences = {}
    with open(f, 'r') as file:
        for line in file:
            if line.startswith('>'):
                name = line.rstrip()
                sequences[name] = ''
            else:
                seq = line.rstrip()
                check_dna(seq)
                sequences[name] += seq
    return sequences

# Test
# read_fasta('dna.fa')
# read_fasta('dna2.fa')
# read_fasta('dna_invalid_char.fa')
# read_fasta('dna_malformat.fa')


def add_to_database(d,f):
    '''Reads a FASTA file f and adds its sequences to dictionary d.'''
    sequences = read_fasta(f)
    d[f] = sequences
    return d

# Test

#d = {}
#d = add_to_database(d, 'dna.fa')
#d = add_to_database(d, 'dna2.fa')
#print(d)



# Task 2: Analyzing all records from a species

def filter_seqs(database, species):
    '''Returns a dictionary with sequences from a given species.'''
    filtered = {}
    for file in database:
        for name in database[file]:
            if species in name:
                filtered[name] = database[file][name]
    return filtered

# Test

#mus = filter_seqs(d, 'Mus musculus')
#print(mus)

def total_sequence_length(d):
    '''Returns the total length of the sequences in a dictionary.'''
    # Raise an error if the input is not a dictionary
    if type(d) is not dict:
        raise ValueError("Input must be a dictionary")
    total = 0
    for seq in d.values():
        total += len(seq)
    
    return total

# Test

# total_sequence_length(mus)
# 26
# total_sequence_length({'s1' :'' ,'s2': 'CAAAACA'})
# 7
# total_sequence_length({})
# 0
# total_sequence_length('hello')
# ValueError: Input must be a dictionary



# Task 3: Writing a dictionary to a fasta file

def write_fasta(d, f):
    '''Writes a dictionary of sequences to a FASTA file.'''
    with open(f, 'w') as file:
        for name, seq in d.items():
            file.write(name + '\n')
            file.write(seq + '\n')

# Test

# write_fasta(mus, 'mus_only.fa')



# Task 4: Putting it all together

def main():
    d = {}
    print("(a) add a file to the database;")
    print("(b) print the length of all sequences of a given species;")
    print("(c) write out a fasta file of all sequences of a given species;")
    print("(q) quit;")
    while True:
        opt = input("Provide an option: ")
        if opt == 'a':
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
            species = input("Which species: ")
            filtered = filter_seqs(d, species)
            print(total_sequence_length(filtered))
        elif opt == 'c':
            species = input("Enter the species: ")
            filepath = input("Which file path: ")
            filtered = filter_seqs(d, species)
            write_fasta(filtered, filepath)
            print("File saved.")
        elif opt == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")




main()









