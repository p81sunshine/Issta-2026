from solution import *

def test_example_1():
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    expected = [[1,2,10],[4,5,7,8]]
    assert findWinners(matches) == expected, "Example 1 failed"

def test_example_2():
    matches = [[2,3],[1,3],[5,4],[6,4]]
    expected = [[1,2,5,6],[]]
    assert findWinners(matches) == expected, "Example 2 failed"

def test_case_3():
    matches = [[1,2], [2,3], [3,4], [4,5]]
    expected = [[1], [2,3,4,5]]
    assert findWinners(matches) == expected, "Test case 3 failed"

def test_case_4():
    matches = [[1,2], [2,1], [3,4]]
    expected = [[3], [1,2,4]]
    assert findWinners(matches) == expected, "Test case 4 failed"