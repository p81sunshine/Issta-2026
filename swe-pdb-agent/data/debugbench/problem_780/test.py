from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Test case 1 failed: input 5 should return 2"

def test_example_2():
    assert findComplement(1) == 0, "Test case 2 failed: input 1 should return 0"

def test_case_num_2():
    assert findComplement(2) == 1, "Test case for input 2 failed"

def test_case_num_6():
    assert findComplement(6) == 1, "Test case for input 6 failed"

def test_case_num_4():
    assert findComplement(4) == 3, "Test case for input 4 failed"