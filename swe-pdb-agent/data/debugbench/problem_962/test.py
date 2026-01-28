from solution import *

def test_example_1():
    assert numPermsDISequence("D") == 1, "Example 1: Input 'D' should return 1"

def test_example_2():
    assert numPermsDISequence("DID") == 5, "Example 2: Input 'DID' should return 5"

def test_empty_input():
    assert numPermsDISequence("") == 1, "Edge case: Empty string should return 1"

def test_di_sequence():
    assert numPermsDISequence("DI") == 2, "Test case 'DI' should return 2"