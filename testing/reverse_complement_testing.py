#!/usr/bin/env python3 

import pytest

### Definition of a function to reverse complement a DNA sequence
def rev_comp(dna):
    """
    Return the reverse complement of a DNA sequence.
    """
    # Make the complement
    comp = ""
    for nt in dna:
        if nt == "A":
            comp += "T"
        elif nt == "a":
            comp += "t"
        elif nt == "T":
            comp += "A"
        elif nt == "t":
            comp += "a"
        elif nt == "G":
            comp += "C"
        elif nt == "g":
            comp += "c"
        elif nt == "C":
            comp += "G"
        elif nt == "c":
            comp += "g"
        else:
            raise ValueError (f"Invalid nucleotide found: {nt}")
    # Make the reverse
    rev_comp = comp[::-1]
    return rev_comp

### Add tests to make sure function works as expected
def test_rev_comp_lower(): # Testing all lowercase input
    expected = "atgc"
    observed = rev_comp("gcat")
    assert observed == expected, f'Expected is ({expected}), got ({observed}))'

def test_rev_comp_upper(): # Testing all uppercase input
    expected = "TAGCGC"
    observed = rev_comp("GCGCTA")
    assert observed == expected, f'Expected is ({expected}), got ({observed})'

def test_rev_comp_mixed(): # Testing mixed case input
    expected = "agTCAgCtA"
    observed = rev_comp("TaGcTGAct")
    assert observed == expected, f'Expected is ({expected}), got ({observed})'

def test_rev_comp_non_nt():
    try:
        observed = rev_comp("ATCGN")
    except ValueError:
        return
    assert False, 'Expected ValueError exception, got ({observed})'        

