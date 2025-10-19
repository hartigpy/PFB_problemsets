#!/usr/bin/env python3 

### FASTA file parsing
# reads in a FASTA file and stores each FASTA record separately in a dictionary

# make an empty dictionary
fasta_dict = {}
seq_ID = ''
sequence = ''

### open file and test which line is which
with open ("Python_06.fasta", "r") as fasta:
    for line in fasta: # for each line
        line = line.rstrip() # removes the empty character in the end of a line
        if line.startswith(">"): # checks if line starts with >
           seq_ID = line.lstrip(">")
           fasta_dict[seq_ID] = ''
        else:
            fasta_dict[seq_ID] += line # += means add to it
print(f'{fasta_dict}')
