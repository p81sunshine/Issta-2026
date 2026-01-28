from solution import *

def test_example_1():
    assert numPermsDISequence("DID") == 5, "Failed for input 'DID'"

def test_example_2():
    assert numPermsDISequence("D") == 1, "Failed for input 'D'"

def test_empty_string():
    assert numPermsDISequence("") == 1, "Failed for empty input"

def test_id_case():
    assert numPermsDISequence("ID") == 2, "Failed for input 'ID'"

def test_ii_case():
    assert numPermsDISequence("II") == 1, "Failed for input 'II'"