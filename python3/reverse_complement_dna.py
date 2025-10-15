#!/usr/bin/env python3 
import sys

### definition of a DNA sequence variable
dna = sys.argv[1]

### make complement
dna_comp = "" # make an empty string
for nt in dna: # check for each nt
    if nt == "A":
        dna_comp = dna_comp + "T"
    elif nt == "a":
        dna_comp = dna_comp + "t"      
    elif nt == "T":
        dna_comp = dna_comp + "A"
    elif nt == "t":
        dna_comp = dna_comp + "a"   
    elif nt == "G":
        dna_comp = dna_comp + "C"
    elif nt == "g":
        dna_comp = dna_comp + "c"  
    elif nt == "C":
        dna_comp = dna_comp + "G"
    elif nt == "c":
        dna_comp = dna_comp + "g"  
    else: # a way to check if there are only A, T, G and C
        print(f'This is not a DNA sequence')
        sys.exit() # this will terminate the programe            
print(f'The complement of this sequence is {dna_comp}')

### complement can also be done like this, but this will not retain the original formatting
#dna_comp = dna_upper.replace("A", "t").replace("T", "a")
#print(dna_comp.upper())

### make reverse
dna_rev = dna_comp[::-1]
print(f'The reverse complement og this sequence is {dna_rev}')