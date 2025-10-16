#!/usr/bin/env python3 

### Open, read and write contents of a file
with open ("Python_06.txt", "r") as python6_read, open("Python_06_uc.txt", "w") as python6_write: # opens two fileas as objects, one for reading, one for writing
    for line in python6_read:
        #line = line.rstrip() # removes new line from input file, not necessary in this case
        line_up = line.upper() # makes every line uppercase
        python6_write.write(f'{line_up}') # writes to new file, new line included from read-file as I did not strip it away


print(f'Wrote to new file')