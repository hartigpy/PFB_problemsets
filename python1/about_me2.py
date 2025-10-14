#!/usr/bin/env python3 

# now using the special built-in list sys.argv
import sys

my_name = sys.argv[1]
my_fav_color = sys.argv[2]
my_fav_activity = sys.argv[3]
my_fav_animal = sys.argv[4]

# now uding + to separate print arguments
print("My name: " + my_name) 
print("My favorite color: " + my_fav_color)
print("My favorite activity: " + my_fav_activity)
print("Mz favorite animal: " + my_fav_animal)

# when running this script it is necessary to add content in the command line
# ./about_me2.py Yael Black Coding Dog