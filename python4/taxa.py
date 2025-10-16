#!/usr/bin/env python3 

taxa_string = "sapiens : erectus : neanderthalensis"
print(f'This is a {type(taxa_string)} containing {taxa_string}')

taxa_list = taxa_string.split(' : ')
print(f'This is a {type(taxa_list)} containing {taxa_list}')
print(taxa_list[1])

taxa_list_sorted_ascii = sorted(taxa_list, key=None, reverse=False)
print(taxa_list_sorted_ascii)

taxa_list_sorted_length = sorted(taxa_list, key=len, reverse=False)
print(taxa_list_sorted_length)