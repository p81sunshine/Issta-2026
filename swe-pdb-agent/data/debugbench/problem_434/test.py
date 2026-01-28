from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Test case 1 failed: input 5 should return 2"

def test_example_2():
    assert findComplement(1) == 0, "Test case 2 failed: input 1 should return 0"

def test_case_3():
    assert findComplement(2) == 1, "Test case 3 failed: input 2 should return 1"

def test_case_4():
    assert findComplement(6) == 1, "Test case 4 failed: input 6 should return 1"

def test_case_5():
    assert findComplement(10) == 5, "Test case 5 failed: input 10 should return 5"