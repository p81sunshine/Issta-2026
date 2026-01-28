from solution import *

def test_example_1():
    assert minEatingSpeed([3,6,7,11], 8) == 4, "Example 1 failed"

def test_example_2():
    assert minEatingSpeed([30,11,23,4,20], 5) == 30, "Example 2 failed"

def test_example_3():
    assert minEatingSpeed([30,11,23,4,20], 6) == 23, "Example 3 failed"

def test_single_pile_case():
    assert minEatingSpeed([10], 1) == 10, "Single pile with exact hours failed"

def test_single_pile_with_larger_hours():
    assert minEatingSpeed([10], 5) == 2, "Single pile with larger hours failed"