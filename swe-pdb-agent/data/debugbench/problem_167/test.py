from solution import *

def test_example_1():
    assert findMaximumElegance([[3,2],[5,1],[10,1]], 2) == 17

def test_example_2():
    assert findMaximumElegance([[3,1],[3,1],[2,2],[5,3]], 3) == 19

def test_example_3():
    assert findMaximumElegance([[1,1],[2,1],[3,1]], 3) == 7

def test_infinite_loop_case():
    # This case triggers infinite loop in buggy code but works in correct code
    items = [[15,1],[20,1],[10,2],[15,2],[5,3],[10,3]]
    assert findMaximumElegance(items, 3) == 54

def test_edge_case_single_category():
    # Test when all items are in the same category
    assert findMaximumElegance([[10,1],[20,1],[30,1]], 3) == 60 + 1**2  # 60+1=61