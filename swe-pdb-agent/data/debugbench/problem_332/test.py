from solution import *

def test_example_1():
    assert numPermsDISequence("DID") == 5, "Test case 'DID' should return 5"

def test_example_2():
    assert numPermsDISequence("D") == 1, "Test case 'D' should return 1"

def test_case_i():
    assert numPermsDISequence("I") == 1, "Test case 'I' should return 1"

def test_case_di():
    assert numPermsDISequence("DI") == 2, "Test case 'DI' should return 2"