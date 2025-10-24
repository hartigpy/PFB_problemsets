#!/usr/bin/env python3 

### Open and read the contents of a file
with open ("Python_06.seq.txt", "r") as read_obj, open("Python_06_fasta_rev.seq.txt", "w") as write_obj: # opens two file as an object, one for reading, one for writing
    for line in read_obj: # for each line of the object reading in
        line_items = line.rstrip().split("\t") # removes line and splits string at \t, returns a list with object left of the \t as 0 and right of the \t as 1
        seq = line_items[1] # assigning list item at index 1 (sequence) to variable
        seq_rev = seq[::-1] # reverses sequence
        seq_rev_comp = seq_rev.replace("A", "t").replace("T", "A").replace("G", "c").replace("C", "g") # generates complement
        seq_up = seq_rev_comp.upper() # makes each line uppercase
        write_obj.write(f'> {line_items[0]}\n{seq_up}\n') # writes list item 0 (sequence name) and seq
    

print(f'Done')