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
count_C = dna_upper.count("C")ion of 