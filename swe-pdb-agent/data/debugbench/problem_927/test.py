from solution import *

def test_example_1():
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    expected = [[1,2,10],[4,5,7,8]]
    assert findWinners(matches) == expected, "Failed to correctly identify players with zero or one loss"

def test_example_2():
    matches = [[2,3],[1,3],[5,4],[6,4]]
    expected = [[1,2,5,6],[]]
    assert findWinners(matches) == expected, "Failed to handle multiple players with same loss count"

def test_single_match():
    matches = [[1,2]]
    expected = [[1],[2]]
    assert findWinners(matches) == expected, "Failed for single match scenario"

def test_multiple_wins_with_losers():
    matches = [[1,2],[1,3],[1,4]]
    expected = [[1],[2,3,4]]
    assert findWinners(matches) == expected, "Failed to distinguish between win counts and loss counts"