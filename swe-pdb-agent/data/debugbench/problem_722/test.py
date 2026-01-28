from solution import *

def test_example_1():
    assert numPermsDISequence("D") == 1, "Example 1 failed"

def test_example_2():
    assert numPermsDISequence("DID") == 5, "Example 2 failed"

def test_case_i():
    assert numPermsDISequence("I") == 1, "Test case for 'I' failed"

def test_case_id():
    assert numPermsDISequence("ID") == 2, "Test case for 'ID' failed"