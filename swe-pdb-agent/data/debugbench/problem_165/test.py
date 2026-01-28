from solution import *

def test_example_1():
    assert numPermsDISequence("D") == 1, "Failed for input 'D'"

def test_example_2():
    assert numPermsDISequence("DID") == 5, "Failed for input 'DID'"

def test_increasing_case():
    assert numPermsDISequence("I") == 1, "Failed for increasing sequence 'I'"

def test_id_case():
    assert numPermsDISequence("ID") == 2, "Failed for input 'ID'"

def test_di_case():
    assert numPermsDISequence("DI") == 2, "Failed for input 'DI'"