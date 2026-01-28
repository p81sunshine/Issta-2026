from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Input: num=5 should return 2"

def test_example_2():
    assert findComplement(1) == 0, "Input: num=1 should return 0"

def test_case_num_2():
    assert findComplement(2) == 1, "Input: num=2 (binary 10) should return 1 (complement 01)"

def test_case_num_4():
    assert findComplement(4) == 3, "Input: num=4 (binary 100) should return 3 (complement 011)"

def test_case_num_6():
    assert findComplement(6) == 1, "Input: num=6 (binary 110) should return 1 (complement 001)"