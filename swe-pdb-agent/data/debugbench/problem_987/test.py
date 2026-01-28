from solution import *

def test_example_1():
    assert numPermsDISequence("DID") == 5, "Failed for input 'DID'"

def test_example_2():
    assert numPermsDISequence("D") == 1, "Failed for input 'D'"

def test_case_i():
    assert numPermsDISequence("I") == 1, "Failed for input 'I'"

def test_case_id():
    assert numPermsDISequence("ID") == 2, "Failed for input 'ID'"

def test_empty_string():
    assert numPermsDISequence("") == 1, "Failed for empty input"