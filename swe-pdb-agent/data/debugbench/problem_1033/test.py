from solution import *

def test_example_1():
    assert closestCost([1,7], [3,4], 10) == 10, "Example 1 should return 10"

def test_example_2():
    assert closestCost([2,3], [4,5,100], 18) == 17, "Example 2 should return 17"

def test_example_3():
    assert closestCost([3,10], [2,5], 9) == 8, "Example 3 should return 8"

def test_edge_case_no_toppings():
    assert closestCost([5], [], 5) == 5, "No toppings should return base cost"

def test_case_over_target():
    assert closestCost([3], [5], 7) == 8, "Should choose 8 as it's closer to 7 than 3"