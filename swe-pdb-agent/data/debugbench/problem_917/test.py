from solution import *

def test_example_1():
    assert numPermsDISequence("DID") == 5, "Failed for 'DID' case"

def test_example_2():
    assert numPermsDISequence("D") == 1, "Failed for 'D' case"

def test_case_i():
    assert numPermsDISequence("I") == 1, "Failed for 'I' case"

def test_case_di():
    assert numPermsDISequence("DI") == 2, "Failed for 'DI' case"

def test_empty_string():
    assert numPermsDISequence("") == 1, "Failed for empty string"