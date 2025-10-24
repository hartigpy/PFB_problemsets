#!/usr/bin/env python3 

import sys

### Parsing BLAST tabular output format to extract informaion
### Specify parameters (lenght and scoring matrix) via command line
### Evaluate accuracy of similarity statistics

# Getting input from the command line
length = sys.argv[1] # "rand5-200", "rand5-800"
scoring_matrix = sys.argv[2] # "BLOSUM62", "BLOSUM80, "PAM30", "PAM70"
file = f'input/blast_{length}_v_qfo_{scoring_matrix}.txt'
print(file)         

query_list = []

# Parsing through the files
with open (file, "r") as file:
        for line in file:
            query = {}
            line = line.rstrip() # to remove the newline character
            if line.startswith("#"): # to skip the lines with #
                continue
            else: # to break each line into different fields
                query['qseqid'] = line.split('\t')[0]
                query['sseqid'] = line.split('\t')[1]
                query['percid'] = line.split('\t')[2]
                query['alen'] = line.split('\t')[3]
                query['mismat'] = line.split('\t')[4]
                query['gaps'] = line.split('\t')[5]
                query['q_start'] = line.split('\t')[6]
                query['q_end'] = line.split('\t')[7]
                query['s_start'] = line.split('\t')[8]
                query['s_end'] = line.split('\t')[9]
                query['evalue'] = line.split('\t')[10]
                query['bits'] = line.split('\t')[11]
                print(query)
       

# Evaluate                 