from solution import *

def test_example_1():
    assert minOperationsMaxProfit([8, 3], 5, 6) == 3, "Failed for first example"

def test_example_2():
    assert minOperationsMaxProfit([10, 9, 6], 6, 4) == 7, "Failed for second example"

def test_example_3():
    assert minOperationsMaxProfit([3, 4, 0, 5, 1], 1, 92) == -1, "Failed for third example"

def test_tie_case():
    # This case creates a profit tie between round 1 and 2, correct code returns earliest (1)
    assert minOperationsMaxProfit([4, 1], 2, 2) == 1, "Failed to handle profit tie correctly"