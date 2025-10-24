#!/usr/bin/env python3 

### Find every occurence of 'Nobody' and print the position

import re # to be able to use re. methods

line_num = 0

with open ("Python_07_nobody.txt", "r") as nobody_obj: # opens the file to read
    for line in nobody_obj:
        line_num = line_num + 1
        for found in re.finditer(r"Nobody", line):
            where = found.group()
            where_start = found.start() + 1
            where_end = found.end() + 1
            print(f'Found {where} in line {line_num}, it starts at position {where_start} and ends at {where_end}')
            

### Substitute every 'Nobody' with a something and write this to an output file
with open ("Python_07_nobody.txt", "r") as read_file, open ("Python_07_somebody", "w") as write_file:
    for line in read_file:
        new_line = re.sub(r'Nobody', r'Somebody', line)
        write_file.write(new_line)
    print(f'done')        