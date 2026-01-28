from solution import *

def test_example_1():
    assert find_complement(5) == 2, "Example 1: 5 (101) should return 2 (010)"

def test_example_2():
    assert find_complement(1) == 0, "Example 2: 1 (1) should return 0 (0)"

def test_num_2():
    assert find_complement(2) == 1, "Case 2: 2 (10) should return 1 (01)"

def test_num_7():
    assert find_complement(7) == 0, "Case 7: 7 (111) should return 0 (000)"

def test_num_4():
    assert find_complement(4) == 3, "Case 4: 4 (100) should return 3 (011)"