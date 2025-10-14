#!/usr/bin/env python3 
import sys

count = int(sys.argv[1])

if count > 0: # tests if the number is positive
    print(count, "is positive") 
    if count < 50: # tests if the number is below 50
        if count % 2 == 0: # tests if the number is even
            print(count, "is less than 50 and an even number")
        else:
            print(count, "is less than 50 and an odd number")
    if count > 50: # tests if the number is above 50
        if count % 3 == 0: # tests if the number is divisiable by 3
            print(count, "is larger than 50 and is divisable by 3")   
        else:
            print(count, "is larger than 50 and is not divisiable by 3")    
    if count == 50: # tests if the number is exactly 50
        print(count, "is exactly 50")  
elif count == 0: # tests if the number is exactly 0
    print(count, "is 0")
else:
    print(count, "is negative")
