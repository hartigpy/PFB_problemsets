#!/usr/bin/env python3 
import sys

### Create a function to format a string of DNA so that each line is no more than 60 nt lng

## Read in variables and give user instructions on what to enter as input
dna_string = ''
try:
    dna_string = sys.argv[1]
    print("User provided DNA sequence:", dna_string)
except:
    print("Please provide a DNA sequence")

width = ''
try:
    width = int(sys.argv[2])
    print("User provided maximum length of line:", width)
except:
    print("Please provide maximum length of line")     

## Create the function to return chunks of provided maximum width
def dna_width_nt(dna):
    dna_chunk = []
    i = 0
    dna = dna.replace("\n", "")
    while i < len(dna):
        dna_chunk.append(dna[i:i+width])
        i += width
        #print(i)
    dna_chunk_string = '\n'.join(dna_chunk) # joining of list items in a string with \n
    return(dna_chunk_string)

## Call the function
print(f'This is the provided DNA sequence split according to the maximum length:')
print(f'{dna_width_nt(dna_string)}')