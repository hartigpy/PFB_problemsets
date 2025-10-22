#!/usr/bin/env python3 

import pytest

### Definition of a function to reverse complement a DNA sequence
def reverse_complement(dna):
    """
    Return the reverse complement of a DNA sequence, preserving case.
    Raises a ValueError if the sequence contains invalid characters.
    """
    # Make the complement
    complement = ""
    for nt in dna:
        if nt == "A":
            complement += "T"
        elif nt == "a":
            complement += "t"
        elif nt == "T":
            complement += "A"
        elif nt == "t":
            complement += "a"
        elif nt == "G":
            complement += "C"
        elif nt == "g":
            complement += "c"
        elif nt == "C":
            complement += "G"
        elif nt == "c":
            complement += "g"
        else:
            raise ValueError(f"Invalid nucleotide found: {nt}")
    # Make the reverse
    rev_comp = complement[::-1]
    return rev_comp