from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Test case 1 failed"

def test_example_2():
    assert findComplement(1) == 0, "Test case 2 failed"

def test_case_3():
    assert findComplement(2) == 1, "Test case 3 failed"

def test_case_4():
    assert findComplement(4) == 3, "Test case 4 failed"

def test_case_5():
    assert findComplement(6) == 1, "Test case 5 failed"