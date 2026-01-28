from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Example 1 failed"

def test_example_2():
    assert findComplement(1) == 0, "Example 2 failed"

def test_edge_case_zero_complement():
    assert findComplement(3) == 0, "Failed for number with all bits 1"

def test_medium_number():
    assert findComplement(10) == 5, "Failed for medium-sized number"

def test_single_bit_number():
    assert findComplement(2) == 1, "Failed for single-bit complement case"