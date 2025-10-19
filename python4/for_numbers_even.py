#!/usr/bin/env python3 

### Iterate through each element of a list using a for loop and return only the values that are even
numbers = [101,2,15,22,95,33,2,27,72,15,52]
even = []
i = 0

for number in numbers:
    if number %2 == 0:
        even.append(number)

print(even)        
    