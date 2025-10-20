#!/usr/bin/env python3 
import sys

### Create a function to format a string of DNA so that each line is no more than 60 nt lng

## Read in variables and give user instructions on what to enter as input
dna_string = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''    

## Create the function to return 60 nt chunks
def dna_60_nt(dna):
    dna_chunk = []
    i = 0
    dna = dna.replace("\n", "")
    while i < len(dna):
        dna_chunk.append(dna[i:i+60])
        i += 60
        #print(i)
    dna_chunk_string = '\n'.join(dna_chunk) # joining of list items in a string with \n
    return(dna_chunk_string)

## Call the function
print(f'This is the provided DNA sequence split according to the maximum length of 60 nt:')
print(f'{dna_60_nt(dna_string)}')