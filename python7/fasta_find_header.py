#!/usr/bin/env python3 
import re

fasta_dict = {}
header = ''
descr = ''
sequence = ''


### Find all FASTA header lines using pattern matching
# FASTA header line: >seqname description
with open ("Python_07.fasta", "r") as fasta:
    for line in fasta: # for each line
        line = line.rstrip() # removes empty character after each line
        for match in re.finditer(r'((^\>\S+)\s(.+))', line):
            header = match.group(2)
            descr = match.group(3)
            fasta_dict[header] = ''
            print(f'Found a FASTA header: {header}')
            print(f'Found a FASTA description: {descr}')

