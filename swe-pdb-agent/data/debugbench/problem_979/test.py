from solution import *

def test_example_1():
    assert numPermsDISequence("DID") == 5, "Failed for input 'DID'"

def test_example_2():
    assert numPermsDISequence("D") == 1, "Failed for input 'D'"

def test_empty_string():
    assert numPermsDISequence("") == 1, "Failed for empty string input"

def test_i_case():
    assert numPermsDISequence("I") == 1, "Failed for input 'I'"

def test_di_case():
    assert numPermsDISequence("DI") == 2, "Failed for input 'DI'"