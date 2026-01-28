from solution import *

def test_example_1():
    assert flipgame([1,2,4,4,7], [1,3,4,1,3]) == 2, "First example should return 2"

def test_example_2():
    assert flipgame([1], [1]) == 0, "Second example should return 0"

def test_buggy_1001_case():
    assert flipgame([2], [2]) == 0, "Buggy code returns 1001 but correct code returns 0"

def test_valid_candidate():
    assert flipgame([1,3], [2,4]) == 1, "Minimum valid candidate should be 1"

def test_multiple_valid_candidates():
    assert flipgame([3,2], [4,5]) == 2, "Minimum valid candidate should be 2"