#!/usr/bin/env python3 
import sys

### definition of a DNA sequence variable
dna = sys.argv[1]

### make DNA sequence uppercase
dna_upper = dna.upper()

### definition of EcoRI restriction site
motif = "GAATTC"

motif_pos = dna_upper.find(motif)
print(f'found EcoRImotif in start-position: {motif_pos+1} and end-position: {motif_pos+len(motif)+1}') 