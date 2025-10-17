#!/usr/bin/env python3 

### FASTQ File Parsing
## line 1 = @SEQ-ID
## line 2 = sequence
## line 3 = +
## line 4 = quality score in ASCII characters

### Definition of the type of lines that are existing
num_lines = 0
num_seq_id = 0
num_char = 0
num_nt = 0
num_nt_lines = 0

### Open file and test which line is which
with open ("Python_06.fastq", "r") as fastq:
    for line in fastq: # for each line
        line.rstrip() # removes the empty character in the end of a line
        num_char = num_char + len(line) # add length to the number of characters
        # check if line has sequence ID
        if line.startswith("@") and num_lines % 4 == 0: # checks if it starts with @ and if modulus of line is 0 (1st line in the block of 4 lines
        # check if line has sequence    
        if num_lines % 4 == 1: # checks if the modulus of line is 1 (2nd line in the block of 4 lines)
            num_nt = num_nt + len(line)
            num_nt_lines = num_nt_lines + 1
        # adds one to number of lines after each line operation is finished
        num_lines = num_lines + 1

### Calculate average lengths         
avg_line_length = num_char / num_lines
avg_nt_line_length = num_nt / num_nt_lines     
#### THIS IS NOT FINSHED YET
        
### Print results
print(f'Total number of lines: {num_lines}')
print(f'The total number of SEQ-IDs: {num_seq_id}')
print(f'The total number of characters is: {num_char}')
print(f'The total number of nucleotides: {num_nt}')   
print(f'The average length of all lines: {avg_line_length}')  
print(f'The average length of lines with nucleotides: {avg_nt_line_length}')
