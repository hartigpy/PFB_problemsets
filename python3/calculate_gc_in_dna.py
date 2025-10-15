#!/usr/bin/env python3 
import sys

### definition of a DNA sequence variable
dna = sys.argv[1]

# convert DNA sequence to uppercase
dna_upper = dna.upper()

### count nucleotides
count_A = dna_upper.count("A")
count_T = dna_upper.count("T")
count_G = dna_upper.count("G")
count_C = dna_upper.count("C")

# calculate the AT and GC content
dna_upper_length = len(dna_upper)
content_AT = (count_A + count_T)/(dna_upper_length)
content_GC = (count_G + count_C)/(dna_upper_length)

print(f'The AT content of this sequence is {content_AT:.0%} and the GC content of this sequence is {content_GC:.0%}')