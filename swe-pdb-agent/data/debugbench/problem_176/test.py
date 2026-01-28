from solution import *

def test_example_1():
    assert numWays("10101") == 4, "Should return 4 for input '10101'"

def test_example_2():
    assert numWays("1001") == 0, "Should return 0 for input '1001'"

def test_example_3():
    assert numWays("0000") == 3, "Should return 3 for input '0000'"

def test_additional_case():
    assert numWays("1011") == 2, "Should return 2 for input '1011'"