from solution import *

def test_example_1():
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    expected = [[1,2,10],[4,5,7,8]]
    assert findWinners(matches) == expected, "Example 1 failed"

def test_example_2():
    matches = [[2,3],[1,3],[5,4],[6,4]]
    expected = [[1,2,5,6],[]]
    assert findWinners(matches) == expected, "Example 2 failed"

def test_single_match():
    matches = [[1,2]]
    expected = [[1], [2]]
    assert findWinners(matches) == expected, "Single match test failed"

def test_player_with_multiple_losses():
    matches = [[1,2], [2,3], [3,2]]
    expected = [[1], [3]]
    assert findWinners(matches) == expected, "Test player with multiple losses failed"

def test_player_never_lost():
    matches = [[1,2], [1,3], [1,4]]
    expected = [[1], [2,3,4]]
    assert findWinners(matches) == expected, "Test player never lost failed"