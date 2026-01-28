from solution import *

def test_example_1():
    assert numWays("10101") == 4, "Failed for input '10101'"

def test_example_2():
    assert numWays("1001") == 0, "Failed for input '1001'"

def test_example_3():
    assert numWays("0000") == 3, "Failed for input '0000'"

def test_case_111000():
    assert numWays("111000") == 1, "Failed for input '111000'"