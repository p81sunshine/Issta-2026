from solution import *

def test_example_1():
    assert numPermsDISequence("DID") == 5, "Example 1 failed: 'DID' should return 5"

def test_example_2():
    assert numPermsDISequence("D") == 1, "Example 2 failed: 'D' should return 1"

def test_empty_string():
    assert numPermsDISequence("") == 1, "Empty string test failed: should return 1"

def test_i_case():
    assert numPermsDISequence("I") == 1, "I case test failed: 'I' should return 1"

def test_id_case():
    assert numPermsDISequence("ID") == 2, "ID case test failed: 'ID' should return 2"