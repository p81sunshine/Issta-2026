from solution import *

def test_example_1():
    assert get_maximum_consecutive([1, 3]) == 2, "Should return 2 for [1,3]"

def test_example_2():
    assert get_maximum_consecutive([1, 1, 1, 4]) == 8, "Should return 8 for [1,1,1,4]"

def test_example_3():
    assert get_maximum_consecutive([1, 4, 10, 3, 1]) == 20, "Should return 20 for [1,4,10,3,1]"

def test_empty_list():
    assert get_maximum_consecutive([]) == 1, "Should return 1 for empty list"

def test_single_large_coin():
    assert get_maximum_consecutive([5]) == 1, "Should return 1 for [5]"