#!/usr/bin/env python3 

### Defining a dictionary of favourite things
favs = {
    'Book' : 'The Midnight Library', 
    'Song' : 'Purple',
    'Sport' : 'Yoga'
    }

### Print favourite book
print(favs['Book'])

### Print favourite book but using a variable as key
fav_thing = 'Book'
print(favs[fav_thing])

### Print favourite sport
print(favs['Sport'])

### Add another thing to the dictionary and change the key of fav_thing to that
favs['Organism'] = 'Human'
print(favs)
fav_thing = 'Organism'
print(favs[fav_thing])

### Use a fot loop to print out each key and value of the dictionary
for category in favs:
    answer = favs[category]
    print(f'My favourite {category} is {answer}')

### Take a value from the command line for fav_thing and print the value for that item from the dictionary
import sys
fav_thing = sys.argv[1]
favs['Book'] = fav_thing
print(f'{favs}')


# ### Print out all the keys so that the user knows what to pick from
# for category in favs:
#      answer = favs[category]
#      print(f'The categories to pick from are: {category}')
#      options = favs.keys()    
# print(options)    

# ### Change the value of something in the dictionary
# favs['Organism'] = 'Yeast'
# print(f'{favs}')

# # ### Get the fav_thing from the command line and a new value for that key
# import sys
# fav_key = sys.argv[1]
# fav_thing = sys.argv[2]
# favs[fav_key] = fav_thing
# print(f'{favs}')