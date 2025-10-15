#!/usr/bin/env python3 
import sys

### definition of a DNA sequence variable
dna = sys.argv[1]

### check if DNA sequence needs to be converted to uppercase
if 'a' or 't' or 'g' or 'c' in dna:
    dna_uppercase = dna.upper()
else:
    dna_uppercase = dna

### count nucleotides
count_A = dna_uppercase.count("A")
count_T = dna_uppercase.count("T")
count_G = dna_uppercase.count("G")
count_C = dna_uppercase.count("C")

### print the results
print(f'This sequence has {count_A} A')
print(f'This sequence has {count_T} T')
print(f'This sequence has {count_G} G')
print(f'This sequence has {count_C} C')





