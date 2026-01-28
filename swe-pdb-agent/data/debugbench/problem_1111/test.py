from solution import *

def test_example_1():
    items = [[3,2],[5,1],[10,1]]
    k = 2
    assert findMaximumElegance(items, k) == 17, "Example 1 failed"

def test_example_2():
    items = [[3,1],[3,1],[2,2],[5,3]]
    k = 3
    assert findMaximumElegance(items, k) == 19, "Example 2 failed"

def test_example_3():
    items = [[1,1],[2,1],[3,1]]
    k = 3
    assert findMaximumElegance(items, k) == 7, "Example 3 failed"

def test_case_all_distinct_categories():
    items = [[5,0], [3,1], [4,2], [2,3]]
    k = 3
    assert findMaximumElegance(items, k) == 21, "Test all distinct categories failed"