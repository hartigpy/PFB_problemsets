#!/usr/bin/env python3 
import sys

### definition of a DNA sequence variable
dna = sys.argv[1]

### convert DNA sequence to uppercase
dna_upper = dna.upper()

### extract and print the substring (position 100 - 200)
sub_dna = dna_upper[99:200]
print(sub_dna)

### count nucleotides
count_A = sub_dna.count("A")
count_T = sub_dna.count("T")
count_G = sub_dna.count("G")
count_C = sub_dna.count("C")

# calculate the GC content
sub_dna_length = len(sub_dna)
content_GC = (count_G + count_C)/(sub_dna_length)

print(f'The GC content of this sequence is {content_GC:.0%}')