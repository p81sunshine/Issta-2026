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

def test_all_distinct_categories():
    items = [[10,1],[9,2],[8,3],[7,4],[6,5]]
    k = 3
    assert findMaximumElegance(items, k) == (10+9+8 + 3**2), "All distinct categories test failed"

def test_mixed_optimal_choice():
    items = [[100,1],[90,1],[50,2],[40,3]]
    k = 3
    assert findMaximumElegance(items, k) == (100+90+50 + 2**2), "Mixed optimal choice test failed"