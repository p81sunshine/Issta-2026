from solution import *

def test_example_1():
    assert stoneGameVI([1,3], [2,1]) == 1, "Example 1 should return 1 as Alice wins"

def test_example_2():
    assert stoneGameVI([1,2], [3,1]) == 0, "Example 2 should return 0 for a draw"

def test_example_3():
    assert stoneGameVI([2,4,3], [1,6,7]) == -1, "Example 3 should return -1 as Bob wins"

def test_one_stone():
    assert stoneGameVI([5], [3]) == 1, "Single stone case should return 1 when Alice takes it"

def test_three_stones_case():
    assert stoneGameVI([5,1,1], [1,1,1]) == 1, "Three stones case should return 1 when Alice takes first and third stones"