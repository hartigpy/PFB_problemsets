#!/usr/bin/env python3 
import sys

# definition of a DNA sequence variable
dna = sys.argv[1]

# convert DNA sequence to uppercase
dna_uppercase = dna.upper()

# replace all T with U and print the results
rna = dna_uppercase.replace("T", "U")
print(rna)