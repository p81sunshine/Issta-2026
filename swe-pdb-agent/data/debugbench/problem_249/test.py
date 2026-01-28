from solution import *

def test_example_1():
    assert numPermsDISequence("DID") == 5, "Failed for input 'DID'"

def test_example_2():
    assert numPermsDISequence("D") == 1, "Failed for input 'D'"

def test_empty_string():
    assert numPermsDISequence("") == 1, "Failed for empty input"

def test_I_case():
    assert numPermsDISequence("I") == 1, "Failed for input 'I'"

def test_DI_sequence():
    assert numPermsDISequence("DI") == 2, "Failed for input 'DI'"