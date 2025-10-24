#!/usr/bin/env python3 
import re

### Identify ApoI restriction site R^AATTY
# R is either A or G
# Y is either C or T
with open ("Python_07_ApoI.fasta", "r") as fasta:
    for line in fasta:
        line = line.rstrip() # removes empty character to make it actual sequence  
        
        for match in re.finditer(r"([AG]AATT[CT])", line): 
            match_seq = match.group(1)
            #print(f'This is the match: {match_seq}')
            match_start = match.start() +1
            #print(f'This is the match start: {match_start}')
            match_end = match.end() +1
            #print(f'This is the match end: {match_end}')
            match_beg = match_seq[0]
            match_add = '^'
            match_end = match_seq[1:]
            new_match_list = [match_beg, match_add, match_end]
            new_match = ''.join(new_match_list)
            print(f'This is the match: {match_seq} and this is the new match: {new_match}')
            match_seq_cut = re.sub(match_seq, new_match, line)
            print(f'This is the subbed match: {match_seq_cut}') 

### THIS IS NOT FINISHED                   
