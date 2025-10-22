#!/usr/bin/env python3 

import pytest

### Definition of a function to calculate GC content
def gc_content(seq):
    valid = {'A', 'C', 'G', 'T', 'N'}
    seq = seq.upper()
    if not set(seq).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    if len(seq) == 0:
        return 0
    return (seq.count('G') + seq.count('C')) / len(seq)

### Writing pytest unit tests
def test_gc_content_1(): # Testing for 1.0
    expected = 1.0
    observed = gc_content("GCGC")
    assert observed == expected, f'Expected is ({expected}), got ({observed}))'

def test_gc_content_0(): # Testing for 0.0
    expected = 0
    observed = gc_content("ATAT")
    assert observed == expected, f'Expected is ({expected}), got ({observed})'

def test_gc_content_05(): # Testing for 0.5
    expected = 0.5
    observed = gc_content("ATGC")
    assert observed == expected, f'Expected is ({expected}), got ({observed})'

def test_gc_content_empty_string(): # Testing for empty string
    expected = 0
    observed = gc_content("")
    assert observed == expected, f'Expected is ({expected}), got ({observed})'

def test_gc_content_ValueError(): # Testing for ValueError
    try:
        observed = gc_content("ATGXB")
    except ValueError:
        return
    assert False, f'Expected Value error, got ({observed})'

def test_gc_content_N():
    expected = 0.3
    observed = gc_content("ATGNNNTAGC")
    assert observed == expected, f'Expected is ({expected}), got ({observed})'

def test_gc_content_lowecase():
    expected = 0.25
    observed = gc_content("gattacaa")
    assert observed == expected, f'Expected is ({expected}), got ({observed})'                

### To run the test, type pytest ./gc_content_testing.py       