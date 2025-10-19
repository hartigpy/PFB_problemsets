#!/usr/bin/env python3 

### Write a while loop to calculate the factorial of 10

number_list = [1,2,3,4,5,6,7,8,9,10] # creating a list with numbers from 1-10
factorial = 1
i = 0


# Calculate factorial by multiplying all elements in the list
while i < len(number_list):   
    factorial = factorial * number_list[i]
    i = i + 1
    
print(factorial)