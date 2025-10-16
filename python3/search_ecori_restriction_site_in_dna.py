#!/usr/bin/env python3 
import sys

### definition of a DNA sequence variable
dna = sys.argv[1]

### make DNA sequence uppercase
dna_up = dna.upper()

### definition of EcoRI restriction site
motif = "GAATTC"

### find motif and position on forward strand
motif_pos_fw = dna_up.find(motif)
print(f'found EcoRImotif on forward strand in start-position: {motif_pos_fw+1} and end-position: {motif_pos_fw+len(motif)}') 

### find motif and position on reverse strand
dna_comp = dna_up.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
dna_comp_up = dna_comp.upper()
rev_dna_comp = dna_comp_up[::-1]
motif_pos_rv = rev_dna_comp.find(motif)
print(f'found EcoRImotif on reverse strand in start-position: {motif_pos_rv+1} and end-position: {motif_pos_rv+len(motif)}') 
