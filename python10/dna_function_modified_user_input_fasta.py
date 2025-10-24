#!/usr/bin/env python3 
import sys

### Create a function to format a string of DNA so that each line is no more than 60 nt lng

## Read in variables and give user instructions on what to enter as input

fasta = sys.argv[1]
width = 60 #int(sys.argv[2])

if not fasta.endswith( ('.fa', '.fasta')):
    print("Input file has to end with .fa or .fasta")        

## Create the function to return 60 nt chunks
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

## Format the FASTA file accordingly and call function
#for line in fasta:
    #line = line.rstrip()
    # if line.startswith(">"):
    #     print(line)
    #else:
        #line
        #print(f'{dna_width_nt(fasta)}')    
        

## Call the function
# print(f'This is the provided DNA sequence split according to the maximum length:')
print(f'{dna_width_nt(fasta)}')