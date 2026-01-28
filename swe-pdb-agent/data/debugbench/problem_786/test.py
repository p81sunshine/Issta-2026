from solution import *

def test_example_1():
    assert numPermsDISequence("DID") == 5, "Example 1 failed"

def test_example_2():
    assert numPermsDISequence("D") == 1, "Example 2 failed"

def test_case_di():
    assert numPermsDISequence("DI") == 2, "Test case 'DI' failed"

def test_case_id():
    assert numPermsDISequence("ID") == 2, "Test case 'ID' failed"