#!/usr/bin/env python3 

## Import of BioPython and more
import Bio
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

## Definition of variables
filename = "Python_08.fasta" # contains the path to the file
seq_count = 0 # to count all sequences
nt_count = 0 # to count all nucleotides / the total overall length
avg_len = 0 # to calculate average length
seq_len = [] # to add all sequence lengths to
total_gc = 0 # to calculate total gc
avg_gc = 0 # to calculate average gc
seq_gc = [] # to add all sequence gc contents to

## Creation of file parser with different stats
for record in SeqIO.parse(filename, "fasta"):
    # Add a counter
    seq_count += 1 
    # Define length parameters
    nt_count += len(record)
    avg_len = nt_count / seq_count
    # Add current record length to a list
    seq_len.append(len(record))
    # Define GC parameters
    total_gc += gc_fraction(record)
    avg_gc = total_gc / seq_count
    # Add current record GC to a list
    seq_gc.append(gc_fraction(record))

## Check if length is minimum or maximum
min_len = min(seq_len)
max_len = max(seq_len)

## Check if GC is minimum or maximu,
min_gc = min(seq_gc)
max_gc = max(seq_gc)

## Print results
print(f'Total sequence count: {seq_count}')
print (f'Total number of nucletides: {nt_count}')
print (f'The average length is: {avg_len}')
print(f'The shortest length is: {min_len}')
print(f'The longest length is: {max_len}')
print(f'This is the average GC content: {avg_gc}')
print(f'This is the lowest GC content: {min_gc}')
print(f'This is the highest GC content: {max_gc}')    