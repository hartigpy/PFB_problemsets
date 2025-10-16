#!/usr/bin/env python3 

### Open and read the contents of a file
with open ("Python_06.txt", "r") as python6_obj: # opens the file as an object
     for line in python6_obj:
         line = line.rstrip() # removes the new line from file input
         line_up = line.upper() # makes each line uppercase
         print(line_up) # prints it to the STDOUT