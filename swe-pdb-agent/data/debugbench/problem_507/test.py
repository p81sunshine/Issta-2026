from solution import *

def test_example_1():
    assert maxStrength([3, -1, -5, 2, 5, -9]) == 1350, "Example 1 failed"

def test_example_2():
    assert maxStrength([-4, -5, -4]) == 20, "Example 2 failed"

def test_case_3():
    assert maxStrength([3, -2, 4]) == 12, "Buggy code fails this case"

def test_case_4():
    assert maxStrength([2, -1, 3]) == 6, "Buggy code fails this case"

def test_edge_case():
    assert maxStrength([0]) == 0, "Edge case with single zero failed"