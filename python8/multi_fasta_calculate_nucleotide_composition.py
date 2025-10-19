#!/usr/bin/env python3 

import re

fasta_dict = {} # making an empty dictionary, dictionary for all
seq_id = '' # will be key for the dictionary


with open ("Python_08.fasta", "r") as fasta_obj: # opens the file
    for line in fasta_obj: # goes through line-by-line
        line = line.rstrip()

        # search for seq_ids and add them to the dictionary as a key
        if line.startswith('>'):
            seq_id = re.search(r'(^\>(\S+))', line)
            seq_id = seq_id[2]
            fasta_dict[seq_id] = ''
            nt_count = { # resets the counter in the dictionary within the dictionary to 0 every time
                'A' : 0,
                'T' : 0,
                'G' : 0,
                'C' : 0
            }

        # count nucleotides in each line
        else:
            fasta_dict[seq_id] = nt_count
            nt_count['A'] += line.count('A')
            nt_count['T'] += line.count('T')
            nt_count['G'] += line.count('G')
            nt_count['C'] += line.count('C')

    # print nt counts for each seq_id
    for seq_id in fasta_dict: # prints out the value for each key in the dictionary
        print(f'{seq_id}: A: {fasta_dict[seq_id]['A']}, T: {fasta_dict[seq_id]['T']}, G: {fasta_dict[seq_id]['G']}, C: {fasta_dict[seq_id]['C']}')