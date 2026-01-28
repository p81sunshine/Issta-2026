from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Example 1 failed: 5's complement should be 2"

def test_example_2():
    assert findComplement(1) == 0, "Example 2 failed: 1's complement should be 0"

def test_num_2():
    assert findComplement(2) == 1, "Test case num=2 failed: 2's complement should be 1"

def test_num_4():
    assert findComplement(4) == 3, "Test case num=4 failed: 4's complement should be 3"

def test_num_6():
    assert findComplement(6) == 1, "Test case num=6 failed: 6's complement should be 1"